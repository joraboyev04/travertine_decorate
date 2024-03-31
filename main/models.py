from django.db import models





from django.contrib.auth.models import AbstractUser



class Pictures(models.Model):
    rasm = models.ImageField(upload_to='products')
    narx = models.CharField(max_length=200)

    def __str__(self):
        return self.narx


class Blog(models.Model):
    picture = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.title