from django.db import models
from django.contrib.auth.models import User
from datetime import date

class MyUser(models.Model):

    user = models.OneToOneField(User)
    sex = models.CharField(max_length = 30)
    phonenummber = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 30)
    permission = models.CharField(max_length = 10, default = '1')

    def __unicode__(self):
	       return self.user.username


class Balance(models.Model):

    username = models.CharField(max_length = 30)
    phonenummber = models.CharField(max_length = 30)
    cardnumber = models.CharField(primary_key = True, max_length = 30)
    balance = models.CharField(max_length = 30)

    def __unicode__(self):
	       return self.cardnumber

class UserRoom(models.Model):

    cardnumber = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)

    floorid = models.CharField(max_length = 30)
    roomid = models.CharField(max_length = 30)

    companynum = models.CharField(max_length = 30, default='0')
    daynum = models.CharField(max_length = 30)
    startdate = models.CharField(max_length = 30)
    enddate = models.CharField(max_length = 30)

    #class Meta:
    #    unique_together = ('cardnumber', 'roomid', 'floorid')

class Company(models.Model):

    cardnumber = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30)

    floorid = models.CharField(max_length = 30)
    roomid = models.CharField(max_length = 30)

    startdate = models.CharField(max_length = 30)
    enddate = models.CharField(max_length = 30)
