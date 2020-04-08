from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

heads = (
('Salary', 'Salary'),
('Fee Collection', 'Fee Collection'),
('Current Bill', 'Current Bill'),
('Telephone Bills', 'Telephone Bills'),
('Misllanious', 'Misllanious'),
('Rent', 'Rent'),
('Transportation', 'Transportation'),
('Capitals', 'Capitals'),
('Loans', 'Loans'),
('Advances', 'Advances'),
)

class Dashboard(models.Model):
	heads = models.CharField(choices=heads,max_length=255)
	date = models.DateField(null=True,blank=True)
	expenses_details = models.CharField(max_length=255)
	receviable = models.FloatField(default=0.0)
	payment = models.FloatField(default=0.0)

	def __str__(self):
		return self.expenses_details



