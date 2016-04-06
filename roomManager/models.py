# -*- coding: utf-8 -*-
from django.db import models
from datetime import date

#Room Table
class Room(models.Model):
    floorid = models.CharField(max_length = 20)
    roomid = models.CharField(max_length = 20)
    roomtype = models.CharField(max_length = 20)
    bedtype = models.CharField(max_length = 20)
    roomdescripte = models.CharField(max_length = 20, null = True)
    status = models.CharField(max_length = 20, default = '0')
    maxnum = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20)
    clockprice = models.CharField(max_length = 20)
    price_unit = models.CharField(max_length = 20, default = '元/天')
    clockprice_unit = models.CharField(max_length = 20)

    class Meta:
		unique_together = ('floorid', 'roomid')

    def __unicode__(self):
        return self.floorid +' '+ self.roomid
