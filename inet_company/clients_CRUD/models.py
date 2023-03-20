from django.db import models

# Create your models here.
class Client(models.Model):
    """A person/company who has contracted the service"""

    name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    dni=models.PositiveBigIntegerField()
    email=models.EmailField(blank=True,null=True)
    address=models.CharField(max_length=300)
    phone_number=models.PositiveBigIntegerField()
    type_of_service=models.CharField(max_length=200) # desp puede ser un CHOICES o una FK a otro model
    initial_date=models.DateTimeField(auto_now_add=True)
    discount=models.PositiveSmallIntegerField(blank=True,null=True)
    discount_initial_date=models.DateTimeField(blank=True,null=True)
    discount_end_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name + self.last_name