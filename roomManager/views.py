#coding: utf-8
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from roomManager.models import *
from accounts.models import *
from supfile.views import *
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta, date


#主页显示函数
@csrf_exempt
def index(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    now = today()
    next_day = nextday(1)
    room_list = Room.objects.filter(status = '0')
    temp_list = Room.objects.filter(status = '1')
    room_list2 =[]
    for item in temp_list:

        set1 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid);
        set2 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, startdate__gte= next_day );
        set3 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, enddate__lte= now);

        #print set1.count() , set2.count(), set3.count()
        if set1.count() == set2.count()+set3.count():
            room_list2.append(item)

    content = {'index': 'index', 'user': user, 'room_list':room_list, 'room_list2':room_list2, 'now': now, 'next_day':next_day}
    return render_to_response('roomManager/queryCenter.html', content, context_instance=RequestContext(req))

#查看预定的房间函数
@csrf_exempt
def myRoom(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    room_list = UserRoom.objects.filter(cardnumber = cardnumber)

    content = {'query': 'query', 'user': user, 'myRoom': 'myRoom', 'room_list':room_list}
    return render_to_response('roomManager/listMyRoom.html', content, context_instance=RequestContext(req))

#入住房间确定
@csrf_exempt
def checkIn(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
        return HttpResponseRedirect(reverse("accounts:accounts_login"))

    id = req.GET.get('index', '')
    starttime = req.GET.get('starttime', '')
    endtime = req.GET.get('endtime', '')

    strs1 = starttime.split('-')
    nowday = date(int(strs1[0]), int(strs1[1]), int(strs1[2]))
    strs2 = endtime.split('-')
    nextday = date(int(strs2[0]), int(strs2[1]), int(strs2[2]))
    daynum =  (nextday - nowday).days

    room = Room.objects.get(id = int(id))
    cost = daynum*int(room.price)

    req.session['roomsession'] = room
    req.session['daynum'] = daynum
    req.session['cost'] = cost
    req.session['starttime'] = starttime
    req.session['endtime'] = endtime

    content = {'query': 'query', 'user': user, 'room': room, 'starttime': starttime, 'endtime': endtime, 'daynum': daynum, 'cost': cost}
    return render_to_response('roomManager/checkIn.html', content, context_instance=RequestContext(req))

#房间退订房间显示函数
@csrf_exempt
def checkOut(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''

    room_list = UserRoom.objects.filter(cardnumber = cardnumber)

    content = {'query': 'query', 'checkOut': 'checkOut', 'user': user, 'room_list':room_list}
    return render_to_response('roomManager/checkOut.html', content, context_instance=RequestContext(req))

#房间退订中的删除房间
@csrf_exempt
def deleteRoom(req, id):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
        return HttpResponseRedirect(reverse("accounts:accounts_login"))
    userroom = UserRoom.objects.get(id = id)
    userset_size = UserRoom.objects.filter(floorid = userroom.floorid, roomid = userroom.roomid).count()
    mycompany_list = Company.objects.filter(floorid = userroom.floorid, roomid = userroom.roomid, startdate = userroom.startdate, enddate = userroom.enddate)
    if userset_size == 1:
        room = Room.objects.get(floorid = userroom.floorid, roomid = userroom.roomid)
        room.startdate = "1990-01-01"
        room.enddate = "1990-01-01"
        room.status = '0'
        room.save()
    userroom.delete()
    for item in mycompany_list:
        item.delete()
    room_list = UserRoom.objects.filter(cardnumber = cardnumber)
    content = {'index': 'index', 'user': user, 'room_list':room_list}
    return render_to_response('roomManager/checkOut.html', content, context_instance=RequestContext(req))

#账户付款
@csrf_exempt
def payBalance(req):

    roomsession = req.session.get('roomsession', '')
    cardnumber = req.session.get('cardnumber', '')

    status = ''
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    return HttpResponseRedirect(reverse("accounts:accounts_login"))

    daynum = req.session.get('daynum', '')
    cost = req.session.get('cost', '')
    starttime = req.session.get('starttime', '')
    endtime = req.session.get('endtime', '')

    room = Room.objects.get(floorid = roomsession.floorid, roomid = roomsession.roomid)
    room.status = '1'
    room.startdate = starttime
    room.enddate = endtime
    room.save()
    print daynum
    userroom = UserRoom.objects.get_or_create(cardnumber = cardnumber, username = user.nickname, floorid = roomsession.floorid, roomid = roomsession.roomid, daynum = daynum, startdate=starttime, enddate=endtime)[0]
    print userroom.startdate, userroom.enddate
    mybalance = Balance.objects.get(cardnumber = cardnumber)
    if int(mybalance.balance) >= cost:
        mybalance.balance =  int(mybalance.balance) - cost
        userroom.save()
        mybalance.save()
        status = 'success'
    else:
        status = 'balance_not_enough'
    content = {'query': 'query', 'user': user, 'status': status, 'cost': cost, 'roomsession': roomsession}
    return render_to_response('roomManager/hint.html', content, context_instance=RequestContext(req))

#账户充值函数
@csrf_exempt
def addBalance(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    return HttpResponseRedirect(reverse("accounts:accounts_login"))
    status = ''
    if req.POST:
        post = req.POST
        addbalance = post.get('addbalance', '')
        readdbalance = post.get('readdbalance', '')
        if addbalance == readdbalance:
            mybalance = Balance.objects.get(cardnumber = cardnumber)
            mybalance.balance = int(mybalance.balance) + int(addbalance)
            mybalance.save()
            status = 'success'
            myroom_list= UserRoom.objects.filter(cardnumber = cardnumber)
            content = {'user': user, 'MyInf': 'MyInf', 'query': 'query', 'userbalance': mybalance, 'myroom_list': myroom_list, 'status': status}
            return render_to_response('accounts/MyInf.html', content, context_instance=RequestContext(req))
        else:
            status = 're_err'

    content = {'query': 'query', 'user': user, 'status': status}
    return render_to_response('roomManager/addBalance.html', content, context_instance=RequestContext(req))


#查询中心函数
@csrf_exempt
def queryCenter(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    if req.GET:
        now = req.GET.get('startdate', '')
        next_day = req.GET.get('enddate', '')
    else:
        now = today()
        next_day = nextday(1)

    #room_list = Room.objects.exclude(startdate__lte= nextday, enddate__gte= now)
    room_list = Room.objects.filter(status = '0')
    temp_list = Room.objects.filter(status = '1')
    room_list2 =[]
    for item in temp_list:

        set1 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid);
        set2 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, startdate__gte= next_day );
        set3 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, enddate__lte= now);

        #print set1.count(),set2.count(),set3.count()
        if set1.count() == set2.count()+set3.count():
            room_list2.append(item)

    content = {'query': 'query', 'user': user, 'room_list':room_list, 'room_list2':room_list2, 'now': now, 'next_day':next_day}
    return render_to_response('roomManager/queryCenter.html', content, context_instance=RequestContext(req))

#按不同条件查询房间函数
@csrf_exempt
def queryByRoomId(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    if req.GET:
        now = req.GET.get('startdate', '')
        next_day = req.GET.get('enddate', '')
    else:
        now = today()
        next_day = nextday(1)

    room_list = Room.objects.filter(status = '0')
    temp_list = Room.objects.filter(status = '1')
    room_list2 =[]
    for item in temp_list:

        set1 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid);
        set2 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, startdate__gte= next_day );
        set3 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, enddate__lte= now);

        #print set1.count(),set2.count(),set3.count()
        if set1.count() == set2.count()+set3.count():
            room_list2.append(item)

    content = {'query': 'query', 'queryByRoomId': 'queryByRoomId', 'user': user, 'room_list':room_list, 'room_list2':room_list2, 'now': now, 'next_day':next_day}
    return render_to_response('roomManager/queryByRoomId.html', content, context_instance=RequestContext(req))

@csrf_exempt
def queryByBedType(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    if req.GET:
        now = req.GET.get('startdate', '')
        next_day = req.GET.get('enddate', '')
    else:
        now = today()
        next_day = nextday(1)

    room_list = Room.objects.filter(status = '0')
    temp_list = Room.objects.filter(status = '1')
    room_list2 =[]
    for item in temp_list:

        set1 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid);
        set2 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, startdate__gte= next_day );
        set3 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, enddate__lte= now);

        #print set1.count(),set2.count(),set3.count()
        if set1.count() == set2.count()+set3.count():
            room_list2.append(item)

    content = {'query': 'query', 'queryByBedType': 'queryByBedType', 'user': user, 'room_list':room_list, 'room_list2':room_list2, 'now': now, 'next_day':next_day}
    return render_to_response('roomManager/queryByBedType.html', content, context_instance=RequestContext(req))

def queryByRoomType(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    if req.GET:
        now = req.GET.get('startdate', '')
        next_day = req.GET.get('enddate', '')
    else:
        now = today()
        next_day = nextday(1)

    room_list = Room.objects.filter(status = '0')
    temp_list = Room.objects.filter(status = '1')
    room_list2 =[]
    for item in temp_list:

        set1 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid);
        set2 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, startdate__gte= next_day );
        set3 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, enddate__lte= now);

        #print set1.count(),set2.count(),set3.count()
        if set1.count() == set2.count()+set3.count():
            room_list2.append(item)

    content = {'query': 'query', 'queryByRoomType': 'queryByRoomType', 'user': user, 'room_list':room_list, 'room_list2':room_list2, 'room_list2':room_list2, 'now': now, 'next_day':next_day}
    return render_to_response('roomManager/queryByRoomType.html', content, context_instance=RequestContext(req))

def queryByFloorId(req):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    if req.GET:
        now = req.GET.get('startdate', '')
        next_day = req.GET.get('enddate', '')
    else:
        now = today()
        next_day = nextday(1)

    room_list = Room.objects.filter(status = '0')
    temp_list = Room.objects.filter(status = '1')
    room_list2 =[]
    for item in temp_list:

        set1 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid);
        set2 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, startdate__gte= next_day );
        set3 = UserRoom.objects.filter(floorid = item.floorid, roomid = item.roomid, enddate__lte= now);

        #print set1.count(),set2.count(),set3.count()
        if set1.count() == set2.count()+set3.count():
            room_list2.append(item)

    content = {'query': 'query', 'queryByFloorId': 'queryByFloorId', 'user': user, 'room_list':room_list, 'room_list2':room_list2, 'now': now, 'next_day':next_day}
    return render_to_response('roomManager/queryByFloorId.html', content, context_instance=RequestContext(req))
