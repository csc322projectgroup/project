from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Menu(models.Model):
    menuId = models.CharField(primary_key = True,max_length=100)
    cheffName = models.ForeignKey(User, on_delete=models.CASCADE)
    date_made = models.DateTimeField(default=timezone.now)
    cheffPic = models.URLField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    fPic = models.URLField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

