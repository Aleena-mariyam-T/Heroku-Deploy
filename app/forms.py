from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import addevent,Eventcomment

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



class EventcommentForm(ModelForm):
    class Meta:
        model = Eventcomment
        fields = ['new_comment']