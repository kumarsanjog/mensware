from django.db import models

# Create your models here.
class customer_register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=15)