from multiprocessing import context
import stat
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from requests import request, session
from .models import Ticket_types, addevent, Payment,Eventcomment,contactus
from .forms import addeventForm,EventcommentForm
from django.views import View
from django.views.generic import TemplateView, View, DetailView,CreateView
import stripe
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

# class MytemplateView(TemplateView):
#     template_name = 'app/index.html'
#     def get_context_data(self,**kwargs):
#         context = super(MytemplateView, self).get_context_data(**kwargs)


def MytemplateView(request):
    event_list = addevent.objects.all()

    # pagination
    p = Paginator(addevent.objects.all(),3)
    page = request.GET.get('page')
    events = p.get_page(page)
    # context['all_events'] = addevent.objects.all()
    context = {
        'all_events': addevent.objects.all(),
        'events': events
    }
    return render(request, "app/Home.html", context)

def about(request):
    pass
    return render(request,"app/about.html")
# logout view
class LogoutView(View):
    def get(self, request):
        messages.success(request, "You Logged out")
        logout(request)

        return HttpResponseRedirect('/')


def detailedview(request, pk):
    event_details = addevent.objects.filter(id=pk)
    print(event_details)
    context = {
        'event_details': event_details
    }
    return render(request, "app/addevent_detail.html", context)


# event view
def eventlist(request):
    pass
    return render(request, "app/eventlist.html")


status = "False"
    
@login_required
def event(request):
    if request.method == "POST":
        form = addeventForm(request.POST,request.FILES)
        if form.is_valid():
            # event_name=form.cleaned_data.get('event_name')
            # if status=="True":
                form.save()
                status = "False"
                return redirect("CheckPaymentView")
        else:
            return render(request,"app/eventaddingform.html",context={"addeventForm":form})
    else:
        form=addeventForm()
        return render(request,"app/eventaddingform.html",context={"addeventForm":form})


# user login

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successfully")
                # return redirect("eventlist")
                return redirect("event")
            # else:
            #     messages.error(request,"Invalid login")
            #     return render(request,"app/login.html",context={"login_form":form})

        else:
            messages.error(request, "Invalid Credentials")
            return render(request, "app/login.html", context={"login_form": form})
    else:
        form = AuthenticationForm()
        return render(request, "app/login.html", context={"login_form": form})
    # except Exception as e:
    #     print(e)
    #     form=AuthenticationForm()
    #     return render(request,"app/login.html",context={"login_form":form})


class CheckPaymentView(TemplateView):
    print("payment view")
    template_name = "app/checkout.html"

    def get_context_data(self, **kwargs):
        print("inside get method")
        # product = Payment.objects.get(Ticket="Gold")
        prices = Payment.objects.filter(Ticket="Gold")
        context = super(CheckPaymentView, self).get_context_data(**kwargs)
        context.update({
            # "product": product,
            "prices": prices
        })
        return context


def successview(request):
    # template_name = "app/success.html"
    status = "True"
    context = {
        'payment_status': 'success'
    }
    return render(request,"app/success.html",context)
        # return redirect("event/CheckPaymentView")
    

    # here we need to save the form adddeventform
    # def get_context_data(self, **kwargs):
        # return super().get_context_data(**kwargs)
        # context = {
        #     'payment_status': 'success'
        # }

        # return context


class CancelView(TemplateView):
    # cancel form and redirect to home
    template_name = "app/cancel.html"

    def get_context_data(self, **kwargs):
        # return super().get_context_data(**kwargs)
        context = {
            'payment_status': 'cancel'
        }
        return context


YOUR_DOMAIN = "http://127.0.0.1:8000"


class CreateCheckoutSessionView(View):
    print("checkoutview functn")

    def post(self, request, *args, **kwargs):
        print("inside post")
        price = Payment.objects.get(id=self.kwargs["pk"])
        print(price)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/successview',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return redirect(checkout_session.url)



def userevents(request):
    print("inside user events")
    if request.method == 'POST':
        print("inside post method",request)
        name = request.POST['Name']
        email = request.POST['Email']
        phone_number = request.POST['phone_number']
        msg = request.POST['msg']
        contactus.objects.create(Name=name,Email=email,phone_number=phone_number,msg=msg)
        print(name)
    return redirect('/')


