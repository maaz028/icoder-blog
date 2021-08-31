from django.db import models

class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11,default='')
    query_txt = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name


# Create your models here.
