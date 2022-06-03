from django.urls import path
from .import views
urlpatterns=[
    # path('',MytemplateView.as_view(template_name="app/index.html")),
    path('',views.MytemplateView.as_view(),name="MytemplateView"),
    path('user_login/',views.user_login,name="user_login"),
    path('event/',views.event,name="event"),
    path('CheckPaymentView/',views.CheckPaymentView.as_view(),name="CheckPaymentView"),
    # path('calculate_order_amount',views.calculate_order_amount),
    # path('create_payment',views.create_payment,name="create_payment"),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.Successview.as_view(), name='success'),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]