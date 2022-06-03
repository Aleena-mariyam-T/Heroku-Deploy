from django.forms import ModelForm
from .models import addevent

class addeventForm(ModelForm):

    class Meta:
        model = addevent
        fields =['event_name',]
