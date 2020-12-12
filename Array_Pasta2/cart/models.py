from django.db import models

# Create your models here.
class menu1(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	food_img = models.URLField()
	
class menu2(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	food_img = models.URLField()
	