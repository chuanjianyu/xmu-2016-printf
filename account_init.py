# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServiceManager.settings')
import django
from accounts.models import *


def population():

    #init room data
    add_user_data('张三', '123456', '男', '11111111111', '362512344911', '2')
    add_user_data('李四', '123456', '女', '11111111112', '362512344912', '2')
    add_user_data('王五', '123456', '男', '11111111113', '362512344913', '2')
    add_user_data('徐二', '123456', '女', '11111111114', '362512344914', '2')



    add_balance_data('张三', '11111111111', '362512344911', 2000)
    add_balance_data('李四', '11111111112', '362512344912', 1000)
    add_balance_data('王五', '11111111113', '362512344913', 100)
    add_balance_data('徐二', '11111111114', '362512344914',3000)

'''

class MyUser(models.Model):

    user = models.OneToOneField(User)
    sex = models.CharField(max_length = 30)
    phonenummber = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 30)
    permission = models.IntegerField(default = '1')
'''

def add_user_data(nickname, password, sex, phonenummber, cardnumber, permission):

    newuser = User.objects.create_user(username=cardnumber, password=password)
    new_myuser = MyUser.objects.get_or_create(user = newuser, sex=sex, phonenummber=phonenummber, nickname=nickname, permission=permission)[0]
    newuser.save()
    new_myuser.save()

'''
class Balance(models.Model):

    username = models.CharField(max_length = 30)
    phonenummber = models.CharField(max_length = 30)
    cardnumber = models.CharField(primary_key = True, max_length = 30)
    balance = models.CharField(max_length = 30)
'''

def add_balance_data(username, phonenummber, cardnumber, balance):

    balance = Balance.objects.get_or_create(username=username, phonenummber=phonenummber, cardnumber=cardnumber, balance=balance)[0]
    balance.save()

### main program
if __name__ == '__main__':
    population()
