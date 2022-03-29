from cProfile import label
from django.db import models

# Create your models here.
class Customer(models.Model):
    services=[
        ('Photography', 'Photography'),
        ('Massage', 'Massage'),
        ('Sexting', 'Sexting'),
        ('Mating', 'Mating'),
        ('Scrubbing', 'Scrubbing'),
        ('Hiking', 'Hiking'),
        ('I can Explain', 'I can Explain'),



    ]
    select=[
    ('Phone call', 'Call Me'),
    ('Massage', 'Massage Me'),
    ('WhatsApp','WhatsApp Me'),
    ('Live Chat','Live Chat'),
    ('Any','Any'),
]

    name =models.CharField(max_length=40, null=True, )
    phone =models.CharField(max_length=15, null=False, blank= False )
    service =models.CharField(max_length=40, choices= services)
    location=models.CharField(max_length=40)
    Service_me_at=models.TimeField(auto_now_add=False,  null=True, blank=True)
    discription =models.TextField(max_length=40, null=True, blank=True)
    created= models.TimeField(auto_now=True)
    reach_me_via=models.CharField(blank=False, null=False,  max_length=30, choices=select)

    def __str__ (self):
        return self.name





    
    