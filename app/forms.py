from django import forms
from django.forms import ModelForm
from .models import addevent,Eventcomment,contactus
from django.core.validators import EMPTY_VALUES
class addeventForm(ModelForm):
    event_name = forms.CharField()
    event_description=forms.CharField(widget=forms.Textarea,required=False)
    event_coordinator = forms.CharField(required=False)
    event_image = forms.ImageField(required=False)
    event_location = forms.CharField(required=False)
    event_start_date = forms.DateTimeField(required=False)
    event_end_date = forms.DateTimeField(required=False)
    class Meta:
        model = addevent
        exclude = ('event_review',)
        fields ='__all__'
    def clean(self, *args, **kwargs):
        event_description = self.cleaned_data.get("event_description",False)
        event_coordinator = self.cleaned_data.get("event_coordinator",False)
        event_image = self.cleaned_data.get("event_image",False)
        event_location = self.cleaned_data.get("event_location",False)
        event_start_date = self.cleaned_data.get("event_start_date",False)
        event_end_date = self.cleaned_data.get("event_start_date",False)

        if not event_description:
            description = self.cleaned_data.get("event_description",None)
            if description in EMPTY_VALUES:
                # raise forms.ValidationError("please enter description")
                self.errors["event_description"]=self.error_class(["Please provide event description"])

        if not event_coordinator:
            co_name = self.cleaned_data.get("event_coordinator",False)
            if co_name in EMPTY_VALUES:
                # raise forms.ValidationError("please enter coordinator name")
                self.errors["event_coordinator"]=self.error_class(["Please provide event Co-ordinator Name "])

        if not event_image:
            event_image = self.cleaned_data.get("event_coordinator",False)
            if event_image in EMPTY_VALUES:
                # raise forms.ValidationError("please enter coordinator name")
                self.errors["event_image"]=self.error_class(["Please upload an image"])

        if not event_location:
            event_location = self.cleaned_data.get("event_location",False)
            if event_location in EMPTY_VALUES:
                # raise forms.ValidationError("please enter coordinator name")
                self.errors["event_location"]=self.error_class(["Please Provide the Location"])
        # return 

        # if not event_start_date:
            event_start_date = self.cleaned_data.get("event_start_date", False)
            if event_start_date in EMPTY_VALUES:
                self.errors["event_start_date"]=self.error_class(["Please Provide the Start Date"])
        
        if not event_end_date:
            event_end_date = self.cleaned_data.get("event_end_date",False)
            if event_end_date in EMPTY_VALUES:
                self.errors["event_end_date"]=self.error_class(["Please Provide the End Date"])
        
        if event_start_date and event_end_date:
            start_date = self.cleaned_data.get("event_start_date", False)
            end_date = self.cleaned_data.get("event_end_date", False)
            if start_date > end_date:
                raise forms.ValidationError("please Provide the Correct Date")
        # else:
            # raise forms.ValidationError("please Provide the Correct")

    # def clean_event_coordinator(self, *args)
class EventcommentForm(ModelForm):
    class Meta:
        model = contactus
        fields ='__all__'