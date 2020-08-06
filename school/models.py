from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date
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
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='Dashboard',null=True,blank=True)
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True,blank=True)
    expenses_details = models.CharField(max_length=255)
    receviable = models.FloatField(default=0.0)
    payment = models.FloatField(default=0.0)
    date_year = models.IntegerField(default=0)
    date_month = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.expenses_details


# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='Dashboard',null=True,blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)


class BRSHDFC(models.Model):
    # Save_file = models.ForeignKey(Document,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='HDFC',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True,blank=True)
    Narration = models.CharField(max_length=255)
    Withdrawal = models.FloatField(default=0.0)
    Deposit = models.FloatField(default=0.0)    
    LedgerDetails = models.CharField(max_length=255)
    date_year = models.IntegerField(default=0,null=True, blank=True)
    date_month = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.Narration
    