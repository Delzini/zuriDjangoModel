from django.db import models
from django.contrib.auth.models import User


 
class Post(models.Model):
        Title = models.CharField(max_length=200, default=None)
        Text = models.TextField(default=None)
        Created_date = models.DateTimeField(default=None)
        Published_date = models.DateTimeField(default=None)
        Author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
         


# Create your models here.




