from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class addevent(models.Model):
    event_name = models.CharField(max_length=100) 
    event_description=models.TextField()
    event_coordinator = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='media/',blank=True, null=True,)
    event_location = models.CharField(max_length=100)
    event_start_date = models.DateTimeField(null=True)
    event_end_date = models.DateTimeField(null=True)
    event_review = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name

Ticket_types=(
    ("Gold","Gold"),
    ("Platinum","Platinum"),
    ("Silver","Silver"),
)
class Payment(models.Model):
    Ticket = models.CharField(max_length=30,choices=Ticket_types,default='Silver')
    price = models.FloatField()
    stripe_product_id = models.CharField(max_length=100)
    stripe_price_id = models.CharField(max_length=100)
    Payment_status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Ticket

class Eventcomment(models.Model):
    comment=models.ForeignKey(addevent, on_delete=models.CASCADE)
    new_comment=models.CharField(max_length=100)


class contactus(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    phone_number=PhoneNumberField()
    msg = models.CharField(max_length=100)

class TempImage(models.Model):
    event_image = models.ImageField(upload_to = 'media/')