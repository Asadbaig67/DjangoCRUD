from django.db import models

# Create your models here.


class Image(models.Model):
    # Define fields for your Image model
    image = models.ImageField(upload_to='user_images/')

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.TextField()
    # image = models.ImageField(upload_to="images/", null=True, blank=True)
    images = models.ManyToManyField(Image)  # Many-to-many relationship

