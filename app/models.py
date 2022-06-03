from django.db import models

# Create your models here.
class addevent(models.Model):
    event_name = models.CharField(max_length=100) 
    event_description=models.TextField()
    event_coordinator = models.CharField(max_length=100)

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
    
    def __str__(self):
        return self.Ticket