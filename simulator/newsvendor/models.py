from django.db import models

# Create your models here.
class question(models.Model):
	qid = models.AutoField(primary_key=True)
	CO = models.PositiveIntegerField()
	CU = models.PositiveIntegerField()
	even = models.BooleanField()
	def __str__(self):
		return f"{self.qid}, CO = {self.CO}, CU = {self.CU}"


class user(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	email = models.EmailField()
	gender = models.CharField(max_length=6)
	age = models.PositiveIntegerField()
	organisation = models.CharField(max_length=128)
	designation = models.CharField(max_length=128)
	def __str__(self):
		return f"{self.name} - {self.email}"

class answer(models.Model):
	uid = models.PositiveIntegerField()
	qid = models.PositiveIntegerField()
	point_forecast = models.PositiveIntegerField()
	LB = models.PositiveIntegerField()
	UB = models.PositiveIntegerField()
	target_fill_rate = models.DecimalField(max_digits=5, decimal_places=2)
	