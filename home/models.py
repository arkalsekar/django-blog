from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    message = models.TextField(max_length=1000)  

    def __str__(self):
        return self.name