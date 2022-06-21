from django.contrib import admin
from .models import addevent,Payment,contactus
# Register your models here.
admin.site.register(addevent),
admin.site.register(Payment),
admin.site.register(contactus)