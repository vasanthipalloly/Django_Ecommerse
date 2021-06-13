from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    des = models.TextField()
    image = models.CharField(max_length=500)
    def __str__(self):
        return self.title

class order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    loc = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username