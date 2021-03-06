# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServiceManager.settings')
import django
from roomManager.models import *


def population():

    #init room data
	add_room_data('一', '101', '特惠商务房', '大床', 2,120, '元/天', 80, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '102', '特惠双床房', '双床', 2,132, '元/天', 100, '元/2小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '103', '商务大床房', '大床', 2,120, '元/天', 60, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '104', '标准双人床', '双床', 2,180, '元/天', 119, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '105', '数码商务床', '单床', 1,178, '元/天', 110, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '106', '大床房', '大床', 2, 154, '元/天', 100, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '107', '数码双人床', '双床', 2,200, '元/天', 130, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('一', '108', '豪华床', '单床', 1, 400, '元/天', 200, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')

	add_room_data('二', '201', '特惠商务房', '大床', 2,120, '元/天', 80, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '202', '特惠双床房', '双床', 2,132, '元/天', 100, '元/2小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '203', '商务大床房', '大床', 2,120, '元/天', 60, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '204', '标准双人床', '双床', 2,180, '元/天', 119, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '205', '数码商务床', '单床', 1,178, '元/天', 110, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '206', '大床房', '大床', 2,154, '元/天', 100, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '207', '数码双人床', '双床', 2,200, '元/天', 130, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('二', '208', '豪华床', '单床', 1,400, '元/天', 200, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')

	add_room_data('三', '301', '特惠商务房', '大床', 2, 120, '元/天', 80, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '302', '特惠双床房', '双床', 2, 132, '元/天', 100, '元/2小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '303', '商务大床房', '大床', 2, 120, '元/天', 60, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '304', '标准双人床', '双床', 2, 180, '元/天', 119, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '305', '数码商务床', '单床', 1, 178, '元/天', 110, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '306', '大床房', '大床', 2, 154, '元/天', 100, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '307', '数码双人床', '双床', 2, 200, '元/天', 130, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('三', '308', '豪华床', '单床', 1, 400, '元/天', 200, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')


	add_room_data('四', '401', '特惠商务房', '大床', 2, 120, '元/天', 80, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '402', '特惠双床房', '双床', 2, 132, '元/天', 100, '元/2小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '403', '商务大床房', '大床', 2, 120, '元/天', 60, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '404', '标准双人床', '双床', 2, 180, '元/天', 119, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '405', '数码商务床', '单床', 1, 178, '元/天', 110, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '406', '大床房', '大床', 2, 154, '元/天', 100, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '407', '数码双人床', '双床', 2, 200, '元/天', 130, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('四', '408', '豪华床', '单床', 1, 400, '元/天', 200, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')

	add_room_data('五', '501', '特惠商务房', '大床', 2, 120, '元/天', 80, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '502', '特惠双床房', '双床', 2, 132, '元/天', 100, '元/2小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '503', '商务大床房', '大床', 2, 120, '元/天', 60, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '504', '标准双人床', '双床', 2, 180, '元/天', 119, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '505', '数码商务床', '单床', 1, 178, '元/天', 110, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '506', '大床房', '大床', 2, 154, '元/天', 100, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '507', '数码双人床', '双床', 2, 200, '元/天', 130, '元/3小时', '建筑面积：16-20平方米;床型：双人床1.8米，1张;最多入住人数：2人;部分床宽是1.5m或1.8m,无洗漱用品')
	add_room_data('五', '508', '豪华床', '单床', 1, 400, '元/天', 200, '元/3小时', '建筑面积：16-20平方米;床型：单人床1.8米，1张;最多入住人数：1人;部分床宽是1.5m或1.8m,无洗漱用品')



'''
class Room(models.Model):
    floorid = models.CharField(max_length = 20)
    roomid = models.CharField(max_length = 20)
    roomtype = models.CharField(max_length = 20)
    bedtype = models.CharField(max_length = 20)
    roomdescripte = models.CharField(max_length = 20, null = True)
    startdate = models.CharField(max_length = 30, null = True)
    enddate = models.CharField(max_length = 30, null = True)
    maxnum = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20)
    clockprice = models.CharField(max_length = 20)
    price_unit = models.CharField(max_length = 20, default = '元/天')
    clockprice_unit = models.CharField(max_length = 20)
'''

def add_room_data(floorid, roomid, roomtype, bedtype, maxnum, price, price_unit, clockprice, clockprice_unit, roomdescripte):

	room = Room.objects.get_or_create(floorid=floorid, roomid=roomid, roomtype=roomtype, bedtype=bedtype, maxnum=maxnum, price=price, price_unit=price_unit, clockprice=clockprice, clockprice_unit=clockprice_unit, roomdescripte=roomdescripte)[0]
	room.save()

### main program
if __name__ == '__main__':
	population()
