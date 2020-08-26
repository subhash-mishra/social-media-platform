from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDataBase(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    Degree = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    profile_title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name



class Connections(models.Model):
    sender = models.ForeignKey(UserDataBase, related_name="sender", on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(UserDataBase, related_name="receiver", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True, default="Sent")
    date = models.DateField(auto_now_add=True, null=True)

class Company_Model(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    map_embad = models.TextField(null=True, blank=True)

class Blogs_Model(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    blog = models.TextField(null=True, blank=True)
    youtube_video = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class BlogLikes(models.Model):
    usr = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey(Blogs_Model, on_delete=models.CASCADE, null=True, blank=True)


















































