#coding=utf-8
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from hashlib import sha1
from .islogin import islogin
from daily_goods.models import GoodsInfo
from daily_order.models import OrderInfo,OrderDetailInfo
from django.core.paginator import Paginator
from daily_cart.models import *
# Create your views here.
def register(request):
    return render(request,'daily_user/register.html')

def register_handle(request):
    post=request.POST
    name=post.get('user_name')
    pwd=post.get('pwd')
    pwd2 = post.get('cpwd')
    email = post.get('email')
    if pwd != pwd2:
        return redirect('/user/register')
    s1=sha1()
    s1.update(pwd.encode('utf-8'))
    pwd3=s1.hexdigest()
    user=UserInfo()
    user.name=name
    user.pwd=pwd3
    user.email=email
    user.save()
    return redirect('/user/login')

def login(request):
    return render(request,'daily_user/login.html')

def login_handle(request):
    post = request.POST
    name = post.get('username')
    pwd = post.get('pwd')
    remember=post.get('remember',0)

    users=UserInfo.objects.filter(name=name)

    if len(users) == 1:
        s1=sha1()
        s1.update(pwd.encode('utf-8'))

        if s1.hexdigest() == users[0].pwd:
            #print(2)
            red = HttpResponseRedirect('/user/info')
            if remember != 0:
                red.set_cookie('name',name)
            else:
                red.set_cookie('name','',max_age = -1)
            request.session['user_id']=users[0].id
            request.session['user_name']=name
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'name': name}
            return render(request, 'daily_user/login.html', context)

    else:
        context={'title':'用户登录','error_name':1,'error_pwd':0,'name':name}
        return render(request,'daily_user/login.html',context)
@islogin
def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).email
    goods_ids = request.COOKIES.get('goods_ids', '')
    #print(goods_ids)
    goods_id_list = goods_ids.split(',')
    #print(goods_id_list)
    goods_list = []
    if len(goods_ids):
        for goods_id in goods_id_list:

            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    #print(goods_list)
    context={
        'title':'用户中心',
        'email':user_email,
        'user_name':request.session['user_name'],
        'page_name': 1, 'info': 1,
        'goods_list': goods_list,
    }
    return render(request,'daily_user/user_center_info.html',context)

def site(request):
    user= UserInfo.objects.get(id=request.session['user_id'])
    #print(1)
    if request.method == 'POST':
        #print(2)
        pos=request.POST
        user.shou=pos.get('shou')
        user.uadr=pos.get('uadr')
        user.post=pos.get('post')
        user.tel=pos.get('tel')
        user.save()
    context={
            'title':'用户中心',
            'user':user
        }
    return render(request,'daily_user/user_center_site.html',context)

def logout(request):
    request.session.flush()
    return redirect('/user/')
#用户中心
@islogin
def user_center_order(request, pageid):
    """
    此页面用户展示用户提交的订单，由购物车页面下单后转调过来，也可以从个人信息页面查看
    根据用户订单是否支付、下单顺序进行排序
    """

    uid = request.session.get('user_id')
    # 订单信息，根据是否支付、下单顺序进行排序
    orderinfos = OrderInfo.objects.filter(
        user_id=uid).order_by('zhifu', '-oid')

    # 分页
    #获取orderinfos list  以两个为一页的 list
    paginator = Paginator(orderinfos, 2)
    #print(paginator)
    # 获取 上面集合的第 pageid 个 值
    orderlist = paginator.page(int(pageid))
    #print(orderlist)
    #获取一共多少 页
    plist = paginator.page_range
    #print(plist)
    #3页分页显示
    qian1 = 0
    hou = 0
    hou2 = 0
    qian2 = 0
    # dd = dangqian ye
    dd = int(pageid)
    lenn = len(plist)
    #print(plist)
    #print(lenn)
    if dd>1:
        qian1 = dd-1
    if dd>=3:
        qian2 = dd-2
    if dd<lenn:
        hou = dd+1
    if  +2<=lenn:
        hou2 = dd+2



    # 构造上下文
    context = {'page_name': 1, 'title': '全部订单', 'pageid': int(pageid),
               'order': 1, 'orderlist': orderlist, 'plist': plist,
               'pre':qian1,'next':hou,'pree':qian2,'lenn':lenn,'nextt':hou2}

    return render(request, 'daily_user/user_center_order.html', context)