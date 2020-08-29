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

class Address_Ledger(models.Model):
    ledger_code = models.CharField(max_length=255, blank=True)
    house_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    colony = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.IntegerField()

    def __str__(self):
        return self.ledger_code

class Dashboard(models.Model):
    address_detail = models.ForeignKey(Address_Ledger,blank=True, null=True,on_delete=models.CASCADE)
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
    