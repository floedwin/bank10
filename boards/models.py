
#from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Myaccount(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description =models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Myaccount.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)


class CurrencyConverter(models.Model):
        amount = models.IntegerField(default=0)
        currency = models.CharField(max_length=200, default=0)
        amount_UGX = models.IntegerField(default=0)


class CustomerBankaccount(models.Model):
    full_name = models.CharField(max_length=200, default='')
    email = models.EmailField(blank=True)
    contact = models.IntegerField(default=0)
    residence = models.CharField(max_length=200, default='')
    work_history = models.CharField(max_length=200, default='')
    identification_information = models.IntegerField(default=0)
    next_of_kin = models.CharField(max_length=200, default='')
    relationship = models.CharField(max_length=200, default='')
    account_number = models.IntegerField(default=0)
    def __str__(self):
        return self.full_name


class LoanCalculator(models.Model):
    amount = models.IntegerField(default=0)
    loan_period = models.CharField(max_length=200, default='')
    interest_rate = models.IntegerField(default=0)
    results = models.IntegerField(default=0)


class Registercustomertranscations(models.Model):
    Full_name = models.CharField(max_length=200, default='')
    Email = models.EmailField(blank=True)
    Contact = models.IntegerField(default=0)
    Account_number = models.IntegerField(default=0)
    Transcation_type = models.CharField(max_length=200, default='')
    Amount = models.IntegerField(default=0)
    Transcation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Full_name

class Registercustomer(models.Model):
        first_name = models.CharField(max_length=200, default='')
        last_name = models.CharField(max_length=200, default='')
        email = models.EmailField(blank=True)
        contact = models.IntegerField(default=0)
        residence = models.CharField(max_length=200, default='')
        occupation = models.CharField(max_length=200, default='')
        next_of_kin = models.CharField(max_length=200, default='')
        relationship = models.CharField(max_length=200, default='')

        def __str__(self):
            return self.first_name


#def __unicode__(self):
    #return self.first_name




