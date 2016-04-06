#coding: utf-8
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import *
from roomManager.models import *
from supfile.models import *
from django.views.decorators.csrf import csrf_exempt

#普通用户登陆函数
@csrf_exempt
def login(req):

	cardnumber = req.session.get('cardnumber', '')
	user = ''
	if cardnumber:
		user = MyUser.objects.get(user__username=cardnumber)
	else:
		HttpResponseRedirect('/')
	status = ''

	if req.POST:
		post = req.POST
		username = post.get('username', '')
		sex = post.get('sex', '')
		phonenummber = post.get('phonenum', '')
		cardnumber = post.get('cardnum', '')
		if MyUser.objects.filter(user__username=cardnumber):
			status = 'user_exist'
		else:
			if MyUser.objects.filter(phonenummber=phonenummber):
				status = 'phone_exist'
			else:
				passwd = cardnumber[len(cardnumber)-6:]#非会员初始默认密码为身份证号码后六位
				newuser = User.objects.create_user(username=cardnumber, password=passwd)
				user = MyUser(user = newuser, nickname=username,sex=sex, phonenummber=phonenummber,permission='1')
				newuser.save()
				user.save()
				req.session['cardnumber'] = cardnumber
				status = 'success'

	content = {'index': 'index', 'user': user, 'status': status}
	return render_to_response('accounts/login.html', content, context_instance=RequestContext(req))

#会员用户登陆函数
@csrf_exempt
def vipLogin(req):

	cardnumber = req.session.get('cardnumber', '')
	if cardnumber:
		user = MyUser.objects.get(user__username=cardnumber)
	else:
		HttpResponseRedirect('/')
	user = ''
	status = ''
	if req.POST:
		post = req.POST
		cardnumber = post.get('cardnumber', '')
		password = post.get('passwd', '')
		#print cardnumber, password
		user = auth.authenticate(username = cardnumber, password = password)
		if user is not None:
			if user.is_active:
				auth.login(req, user)
				req.session['cardnumber'] = cardnumber
				return HttpResponseRedirect('/')
			else:
				status = 'not_active'
		else:
			status = 'not_exist_or_passwd_err'
	content = {'index': 'index', 'user': user, 'status': status}
	return render_to_response('accounts/vipLogin.html', content, context_instance=RequestContext(req))

#用户注销
@csrf_exempt
def logout(req):

	auth.logout(req)
	return HttpResponseRedirect('/')

#更新用户密码函数
@csrf_exempt
def updatepasswd(req):

	cardnumber = req.session.get('cardnumber', '')
	if cardnumber:
		user = MyUser.objects.get(user__username=cardnumber)
	else:
		return HttpResponseRedirect(reverse("accounts:accounts_login"))
	status = ''
	if req.POST:
		post = req.POST
		if user.user.check_password(post.get('old', '')):
			if post.get('new', '') == post.get('new_re', ''):
				user.user.set_password(post.get('new', ''))
				user.user.save()
				status = 'success'
			else:
				status = 're_err'
		else:
			status = 'passwd_err'
	content = {'user': user, 'query': 'query', 'status': status}
	return render_to_response('accounts/setpasswd.html', content, context_instance=RequestContext(req))

#个人基本信息修改函数
@csrf_exempt
def updateInf(req):

	cardnumber = req.session.get('cardnumber', '')
	if cardnumber:
		user = MyUser.objects.get(user__username=cardnumber)
	else:
		return HttpResponseRedirect(reverse("accounts:accounts_login"))
	status = ''
	if user.permission == '2':
		userbalance = Balance.objects.get(cardnumber = cardnumber)
	else:
		userbalance = ''
	#myroom_list = []
	if req.POST:
		post = req.POST
		phonenummber = post.get('phonenummber', '')
		user.phonenummber = phonenummber
		userbalance.phonenummber = phonenummber
		userroom = UserRoom.objects.filter(cardnumber = cardnumber)
		for item in userroom:
			item.phonenummber = phonenummber
			item.save()
			'''
			room = Room.objects.get(floorid = item.floorid, roomid = item.roomid)
			obj = MyRoom( item, room)
			myroom_list.append(obj)
			'''
		myroom_list = UserRoom.objects.filter(cardnumber = cardnumber)
		user.save()
		userbalance.save()
		status = 'success'
		content = {'user': user, 'MyInf': 'MyInf', 'query': 'query', 'userbalance': userbalance, 'status': status, 'myroom_list': myroom_list}
		return HttpResponseRedirect('accounts/MyInf.html', content, context_instance=RequestContext(req))

	content = {'user': user, 'updateInf': 'updateInf', 'query': 'query', 'userbalance': userbalance, 'status': status}
	return render_to_response('accounts/updateInf.html', content, context_instance=RequestContext(req))

#用户信息查看函数
@csrf_exempt
def MyInf(req):

	cardnumber = req.session.get('cardnumber', '')
	if cardnumber:
		user = MyUser.objects.get(user__username=cardnumber)
	else:
		return HttpResponseRedirect(reverse("accounts:accounts_login"))
	if user.permission == '2':
		userbalance = Balance.objects.get(cardnumber = cardnumber)
	else:
		userbalance = ''
	myroom_list= UserRoom.objects.filter(cardnumber = cardnumber)
	'''
	myroom_list = []
	for item in userroom:
		room = Room.objects.get(floorid = item.floorid, roomid = item.roomid)
		obj = MyRoom( item, room)
		myroom_list.append(obj)
		'''
	content = {'user': user, 'MyInf': 'MyInf', 'query': 'query', 'userbalance': userbalance, 'myroom_list': myroom_list}
	return render_to_response('accounts/MyInf.html', content, context_instance=RequestContext(req))

#房间添加同伴
@csrf_exempt
def addCompany(req, id):

	cardnumber = req.session.get('cardnumber', '')
	if cardnumber:
		user = MyUser.objects.get(user__username=cardnumber)
	else:
		return HttpResponseRedirect(reverse("accounts:accounts_login"))

	userroom = UserRoom.objects.get(id=id)
	room = Room.objects.get(floorid = userroom.floorid, roomid = userroom.roomid)
	status = ''
	if req.POST:
		post = req.POST
		addcardnumber = post.get('cardnumber', '')
		addusername = post.get('username', '')
		userroom.companynum = int(userroom.companynum) + 1
		addCompany = Company(cardnumber = addcardnumber, username = addusername, floorid = userroom.floorid, roomid = userroom.roomid, startdate = userroom.startdate, enddate = userroom.enddate)
		addCompany.save()
		userroom.save()
		status = 'success'

	content = {'user': user, 'query': 'query', 'status': status, 'maxadd': int(room.maxnum) - int(userroom.companynum)}
	return render_to_response('accounts/addCompany.html', content, context_instance=RequestContext(req))

#查看预定的房间同伴函数
@csrf_exempt
def listCompany(req, id):

    cardnumber = req.session.get('cardnumber', '')
    if cardnumber:
        user = MyUser.objects.get(user__username=cardnumber)
    else:
	    user = ''
    userroom = UserRoom.objects.get(id=id)
    mycompany_list = Company.objects.filter(floorid = userroom.floorid, roomid = userroom.roomid, startdate = userroom.startdate, enddate = userroom.enddate)

    content = {'query': 'query', 'user': user, 'mycompany_list':mycompany_list}
    return render_to_response('accounts/listCompany.html', content, context_instance=RequestContext(req))
