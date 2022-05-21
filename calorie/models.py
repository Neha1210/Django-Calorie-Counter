from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class foodcal(models.Model):
	foodname=models.CharField(max_length=200,null=True)
	foodcal=models.IntegerField(null=True)

	def __str__(self):
		return self.foodname

class getfoodinfo(models.Model):
	food=models.ForeignKey(foodcal,null=True,on_delete=models.SET_NULL)
	cal=models.IntegerField(null=True,default=0)
	total=models.IntegerField(null=True,default=0)

	def __str__(self):
		return str(self.food)