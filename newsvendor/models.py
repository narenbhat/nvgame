from django.db import models
from jsonfield import JSONField


# Create your models here.
class question(models.Model):
	qid = models.AutoField(primary_key=True)
	data = JSONField(default = list)
	CO = models.PositiveIntegerField()
	CU = models.PositiveIntegerField()
	even = models.BooleanField()
	def __str__(self):
		return f"{self.qid}, CO = {self.CO}, CU = {self.CU} {self.data}"


class user(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	email = models.EmailField()
	gender = models.CharField(max_length=6)
	age = models.PositiveIntegerField()
	organisation = models.CharField(max_length=128)
	designation = models.CharField(max_length=128)
	gamename = models.CharField(default='0000000' ,max_length=128)
	def __str__(self):
		return f"{self.name} - {self.email}"

class answer(models.Model):
	uid = models.PositiveIntegerField()
	qid = models.PositiveIntegerField()
	point_forecast = models.PositiveIntegerField()
	LB = models.PositiveIntegerField()
	UB = models.PositiveIntegerField()
	target_fill_rate = models.DecimalField(max_digits=5, decimal_places=2)
	def __str__(self):
		return f"User = {self.uid}, Q = {self.qid}, Point Forecast = {self.point_forecast}"

class feedback(models.Model):
	uid = models.PositiveIntegerField()
	qid = models.PositiveIntegerField()
	feedback = models.CharField(max_length=4000)
	def __str__(self):
		return f"User = {self.uid}, Q = {self.qid}, Point Forecast = {self.feedback}"
