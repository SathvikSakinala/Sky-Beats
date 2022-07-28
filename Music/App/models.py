from datetime import date
from email.policy import default
from operator import mod
from secrets import choice
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

GENRES = (
        ("0","-"),
        ("1","Pop"),
        ("2","Hip-Hop"),
        ("3","Rock"),
        ("4","Jazz"),
        ("5","Indian"),
        ("6","Dance/Electronic"),
        ("7","Country"),
        ("8","Metal"),
        ("9","K-Pop"),
        ("10","Acoustic"),
    )

class Customer(models.Model):
    
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=False,null=False)
    email= models.EmailField(blank=False,null=False)
    Bio = models.CharField(max_length=30,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    profile_pic = models.ImageField(default="user.png")

class Info(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=False)
    gen1 = models.CharField(max_length=30,choices=GENRES,default=0)
    gen2 = models.CharField(max_length=30,choices=GENRES,default=0)
    gen3 = models.CharField(max_length=30,choices=GENRES,default=0)

    def __str__(self):
        return self.name

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    duration=models.CharField(max_length=20)
    fav = models.BooleanField(default=False)
    genre = models.CharField(max_length = 30,choices=GENRES,default=0)
    paginate_by = 2

    def __str__(self):
        return self.title

    @property
    def get_id(self):
        return self.id

    @property
    def isfav(self):
        return self.fav


'''class Comment(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    song = models.OneToOneField(Song,on_delete=models.SET_NULL,null=True)
    comment = models.TextField(max_length=200,blank=True)
    dateoc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Favourite(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return str(self.id)

class FavouriteItems(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)   
    song = models.OneToOneField(Song,on_delete=models.SET_NULL,null=True)
    favourite = models.ForeignKey(Favourite,on_delete=models.SET_NULL,null=True)
    add = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    @property
    def get_to_know(self):
        Add = self.add
        return Add'''