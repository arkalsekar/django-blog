from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=900)
    slug = models.CharField(max_length=900)
    author = models.CharField(max_length=900, default="Abdul Rehman")
    content = models.TextField()
    tags = models.CharField(max_length=800)
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='images/')


    def __str__(self):
        return self.title
