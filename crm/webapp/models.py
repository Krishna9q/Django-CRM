from django.db import models

# Create your models here.

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
                                         
    def __str__(self):
        return self.first_name +" "+self.last_name
   