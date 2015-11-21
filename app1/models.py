from django.db import models

# Create your models here.
class Flat(models.Model):
	THREE_MONTH = "3 month"
	SIX_MONTH = "6 month"
	NINE_MONTH = "9 month"
	YEAR = "12 month"

	flat_name = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	free_from_date = models.DateTimeField('date free')
	occupied = models.BooleanField()
	period_choices = (
		(THREE_MONTH, '3 months'),
		(SIX_MONTH, '6 months'),
		(NINE_MONTH, '9 months'),
		(YEAR, '12 months'),
	)
	period = models.CharField(max_length = 10, 
								choices = period_choices,
								default = THREE_MONTH)

class Customer(models.Model):
	name = models.CharField(max_length = 200)
	age = models.IntegerField()
	flat = models.ForeignKey(Flat, null = True, blank = True)

