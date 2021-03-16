import threading
from datetime import datetime
import time
from django.http.response import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from app.client import SocketServer
from .forms import CsvForm
from .models import Csv, Num, Numupdate, Report, Sim, Device, Spin,Manage, User
import pandas as pd
from prettytable import PrettyTable
import os
global COMPORT_NAME, sms
import json
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media = os.path.join(BASE_DIR, 'media/')



def index(request):
    res = request.POST.get('update')
    op=Manage.objects.all().last()
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l10=[]
    l11=[]
    l12=[]
    l13=[]
    l14=[]
    l15=[]
    l16=[]
    n = 1
    if res == "Update all ports":
        n = 1
        result = SocketServer.datasend(res)
        if op.types=="8x8":
            obj4 = Sim.objects.all().order_by('-id')[:32][::-1]
            for i in obj4:
                if n <= 8:
                    l1.append(i.pin)
                elif n <= 16:
                    l2.append(i.pin)
                elif n <= 24:
                    l3.append(i.pin)
                elif n <= 32:
                    l4.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n})
        elif op.types=="16x8":
            obj4 = Sim.objects.all().order_by('-id')[:128][::-1]
            for i in obj4:
                if n <= 8:
                    l1.append(i.pin)
                elif n <= 16:
                    l2.append(i.pin)
                elif n <= 24:
                    l3.append(i.pin)
                elif n <= 32:
                    l4.append(i.pin)
                elif n <= 40:
                    l5.append(i.pin)
                elif n <= 48:
                    l6.append(i.pin)
                elif n <= 56:
                    l7.append(i.pin)
                elif n <= 64:
                    l8.append(i.pin)
                elif n <= 72:
                    l9.append(i.pin)
                elif n <= 80:
                    l10.append(i.pin)
                elif n <= 88:
                    l11.append(i.pin)
                elif n <= 96:
                    l12.append(i.pin)
                elif n <= 104:
                    l13.append(i.pin)
                elif n <= 112:
                    l14.append(i.pin)
                elif n <= 120:
                    l15.append(i.pin)
                elif n <= 128:
                    l16.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
        elif op.types=="16x32":
            obj4 = Sim.objects.all().order_by('-id')[:512][::-1]
            for i in obj4:
                if n <= 32:
                    l1.append(i.pin)
                elif n <= 64:
                    l2.append(i.pin)
                elif n <= 96:
                    l3.append(i.pin)
                elif n <= 128:
                    l4.append(i.pin)
                elif n <= 160:
                    l5.append(i.pin)
                elif n <= 192:
                    l6.append(i.pin)
                elif n <= 224:
                    l7.append(i.pin)
                elif n <= 256:
                    l8.append(i.pin)
                elif n <= 288:
                    l9.append(i.pin)
                elif n <= 320:
                    l10.append(i.pin)
                elif n <= 352:
                    l11.append(i.pin)
                elif n <= 384:
                    l12.append(i.pin)
                elif n <= 416:
                    l13.append(i.pin)
                elif n <= 448:
                    l14.append(i.pin)
                elif n <= 480:
                    l15.append(i.pin)
                elif n <= 512:
                    l16.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
        elif op.types=="16x64":
            obj4 = Sim.objects.all().order_by('-id')[:1024][::-1]
            for i in obj4:
                if n <= 64:
                    l1.append(i.pin)
                elif n <= 128:
                    l2.append(i.pin)
                elif n <= 192:
                    l3.append(i.pin)
                elif n <= 256:
                    l4.append(i.pin)
                elif n <= 320:
                    l5.append(i.pin)
                elif n <= 384:
                    l6.append(i.pin)
                elif n <= 448:
                    l7.append(i.pin)
                elif n <= 512:
                    l8.append(i.pin)
                elif n <= 576:
                    l9.append(i.pin)
                elif n <= 640:
                    l10.append(i.pin)
                elif n <= 704:
                    l11.append(i.pin)
                elif n <= 768:
                    l12.append(i.pin)
                elif n <= 832:
                    l13.append(i.pin)
                elif n <= 896:
                    l14.append(i.pin)
                elif n <= 960:
                    l15.append(i.pin)
                elif n <= 1024:
                    l16.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
    elif op.types=="8x8":
        l = 1
        obj = Sim.objects.all().order_by('-id')[:32][::-1]
        for i in obj:
            if l <= 8:
                l1.append(i.pin)
            elif l <= 16:
                l2.append(i.pin)
            elif l <= 24:
                l3.append(i.pin)
            elif l <= 32:
                l4.append(i.pin)
            l += 1
        obj1=Report.objects.all().order_by('-id')[:4][::-1]
        return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4,'si':obj1})
    elif op.types=="16x8":
            obj4 = Sim.objects.all().order_by('-id')[:128][::-1]
            for i in obj4:
                if n <= 8:
                    l1.append(i.pin)
                elif n <= 16:
                    l2.append(i.pin)
                elif n <= 24:
                    l3.append(i.pin)
                elif n <= 32:
                    l4.append(i.pin)
                elif n <= 40:
                    l5.append(i.pin)
                elif n <= 48:
                    l6.append(i.pin)
                elif n <= 56:
                    l7.append(i.pin)
                elif n <= 64:
                    l8.append(i.pin)
                elif n <= 72:
                    l9.append(i.pin)
                elif n <= 80:
                    l10.append(i.pin)
                elif n <= 88:
                    l11.append(i.pin)
                elif n <= 96:
                    l12.append(i.pin)
                elif n <= 104:
                    l13.append(i.pin)
                elif n <= 112:
                    l14.append(i.pin)
                elif n <= 120:
                    l15.append(i.pin)
                elif n <= 128:
                    l16.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
    elif op.types=="16x32":
            obj4 = Sim.objects.all().order_by('-id')[:512][::-1]
            for i in obj4:
                if n <= 32:
                    l1.append(i.pin)
                elif n <= 64:
                    l2.append(i.pin)
                elif n <= 96:
                    l3.append(i.pin)
                elif n <= 128:
                    l4.append(i.pin)
                elif n <= 160:
                    l5.append(i.pin)
                elif n <= 192:
                    l6.append(i.pin)
                elif n <= 224:
                    l7.append(i.pin)
                elif n <= 256:
                    l8.append(i.pin)
                elif n <= 288:
                    l9.append(i.pin)
                elif n <= 320:
                    l10.append(i.pin)
                elif n <= 352:
                    l11.append(i.pin)
                elif n <= 384:
                    l12.append(i.pin)
                elif n <= 416:
                    l13.append(i.pin)
                elif n <= 448:
                    l14.append(i.pin)
                elif n <= 480:
                    l15.append(i.pin)
                elif n <= 512:
                    l16.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
    elif op.types=="16x64":
            obj4 = Sim.objects.all().order_by('-id')[:1024][::-1]
            for i in obj4:
                if n <= 64:
                    l1.append(i.pin)
                elif n <= 128:
                    l2.append(i.pin)
                elif n <= 192:
                    l3.append(i.pin)
                elif n <= 256:
                    l4.append(i.pin)
                elif n <= 320:
                    l5.append(i.pin)
                elif n <= 384:
                    l6.append(i.pin)
                elif n <= 448:
                    l7.append(i.pin)
                elif n <= 512:
                    l8.append(i.pin)
                elif n <= 576:
                    l9.append(i.pin)
                elif n <= 640:
                    l10.append(i.pin)
                elif n <= 704:
                    l11.append(i.pin)
                elif n <= 768:
                    l12.append(i.pin)
                elif n <= 832:
                    l13.append(i.pin)
                elif n <= 896:
                    l14.append(i.pin)
                elif n <= 960:
                    l15.append(i.pin)
                elif n <= 1024:
                    l16.append(i.pin)
                n += 1
            return render(request, 'index/index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})


def csvfile(request):
    form = CsvForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        csv = obj.file_csv
        print(csv)
        op = str(csv)
        final = media+op
        data = pd.read_csv(final)
        data.sort_values("mobile", inplace = True)
        data.drop_duplicates(subset ="mobile",keep ='first', inplace = True) 
        for i in data['mobile']:
            Numupdate.objects.create(name=csv,mobile=i)
        obj=Numupdate.objects.all().filter(name=csv)
        return render(request, 'contacts.html',{'get':obj})
    else:
        form = CsvForm()
        return render(request, 'contacts.html', {'form': form})


def manage(request):
    cname=request.POST.get('cname')
    types=request.POST.get('types')
    print(cname,types)
    if cname!=None and cname!='' and types!=None and types!='':
        print('comming')
        Manage.objects.create(cname=cname,types=types)
        return render(request, 'app_manage.html')
    return render(request, 'app_manage.html')

def device(request):
    global result
    report = ""
    disport = request.POST.get('disconnect_port')
    update = request.POST.get('update')
    if update != None and update!="":
        z = 1
        l1={}
        a="deviceupdate"
        try:
            result = SocketServer.datasend(a)
            print(result)
            obj1=Device.objects.all().order_by('-id')[:4][::-1]
            return render(request, 'manage_device.html', {'get': obj1, 'n': z})
        except Exception as e:
            print(e)
    else:
        obj=Device.objects.all().order_by('-id')[:4][::-1]
        return render(request, 'manage_device.html',{'get':obj})

def model(request):
    return render(request, 'manage_user.html')

def user(request):
    adduser=request.POST.get('add')
    cname=request.POST.get('cname')
    mobile=request.POST.get('mobile')
    uname=request.POST.get('uname')
    # pwd=request.POST.get('password')
    email=request.POST.get('email')
    address=request.POST.get('address')
    pkey=(''.join(str(random.randint(0,9)) for _ in range(12)))
    print(adduser,cname,mobile,uname,email,address,pkey)
    if adduser=="Adduser":
        if cname!=None and cname!='' and mobile!=None and mobile!='' and uname!=None and uname!=''  and email!=None and email!='' and address!=None and address!='' and pkey!=None and pkey!='':
            print('comming')
            User.objects.create(cname=cname,mobile=mobile,uname=uname,email=email,address=address,pkey=pkey)
            get=User.objects.all()
            return render(request, 'user.html',{'get':get})
    get=User.objects.all()
    return render(request, 'user.html',{'get':get})


def compose(request):
    global get
    te = request.POST.get('type')
    conname = request.POST.get('conname')
    number = request.POST.get('mobile')
    message2 = request.POST.get('message')
    li = []
    if te == "list" and conname != None and message2 != None:
        request.session['finame'] = conname
        obj = Num.objects.create(finame=conname, content=message2)
        return render(request, 'compose.html')
    elif te == "list" and conname != None:
        obj = Csv.objects.get(name=conname)
        csv = obj.file_csv
        op = str(csv)
        n = 1
        final = media+op
        with open(final, 'rb') as a:
            a = a.readlines()
            l1 = a[0]
            l1 = l1.decode()
            l1 = l1.split(',')
            t = PrettyTable([l1[0]])
            for i in range(1, len(a)):
                a[i] = a[i].decode()
                t.add_row(a[i].split(','))
                n += 1
            code = t.get_html_string()
            html_file = open('templates/table2.html', 'w')
            html_file = html_file.write(code)
        html_response = render_to_string('table2.html')
        return HttpResponse(html_response, status=200)
    elif te == "list" and conname == None:
        na = Csv.objects.all()
        for i in na:
            na = i.name
            li.append(na)
        data = li
        html_response = render_to_string(
            'select.html', context={'models': data})
        return HttpResponse(html_response, status=200)
    elif te == "manual" and message2 != '' and number != '':
        name = "one"
        get = message.thread(number, message2, name)
        messages.success(request, "message successfully send")
        return render(request, 'compose.html', {'msg': get})
    return render(request, 'compose.html')


def inbox(request):
    global get
    load = request.POST.get('insms')
    if load == "Load_Incoming_SMS":
        get = message.read()
        print(get)
        return render(request, 'inbox.html', {'get': get})
    return render(request, 'inbox.html')


def outbox(request):
    limit = request.POST.get('limit')
    send = request.POST.get('send')
    com=request.GET.get('n')
    sim=request.GET.get('sim')
    finame = request.session['finame'] 
    ajax=request.POST.get('ajax')
    print(ajax)
    li = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l10=[]
    l11=[]
    l12=[]
    l13=[]
    l14=[]
    l15=[]
    l16=[]
    j=0
    k=0
    l=0
    n=0
    m=0
    g=0
    a=0
    z=0
    df=datetime.now()
    op=Manage.objects.all().last()
    if op.types=="8x8":
        if com != None and com!='' and sim!=None and sim!='':
            obj = Num.objects.all().last()
            obj1=Report.objects.all().filter(conname=obj.finame,date__range=["2021-03-11","2021-03-12"],port=com,pin='A')
            for i in obj1:
                j+=1
                if i.status=="success":
                    k+=1
                if i.status=="fail":
                    l+=1
                n=i.limit
            print(j,k,n,obj.finame)
            return render(request, 'sms_out_box1.html', {'get':obj1,'n':n,'l':l,'j':j,'k':k,'port':com,'pin':sim})
        elif limit != None and send != None:
            name = "multi"
            obj1 = Num.objects.all().filter(finame=finame).last()
            conname = obj1.finame
            msg = obj1.content
            print(msg)
            obj = Csv.objects.get(name=conname)
            csv = obj.file_csv
            op = str(csv)
            final = media+op
            read = pd.read_csv(final)
            read.sort_values("mobile", inplace = True)
            read.drop_duplicates(subset ="mobile",keep ='first', inplace = True) 
        
            for i in read['mobile']:
                li.append(i)
                k+=1
            obj1 = Sim.objects.all().order_by('-id')[:32][::-1]
            for i in obj1:
                if n <= 8:
                    l1.append(i.pin)
                elif n <= 16:
                    l2.append(i.pin)
                elif n <= 24:
                    l3.append(i.pin)
                elif n <= 32:
                    l4.append(i.pin)
                n += 1

            com=['COM25','COM26']
            SocketServer.message(conname,com,li, msg, name, limit)
            request.session['finame'] = None
            return render(request, 'outbox/outbox.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4,'k':k})
        elif ajax!=None and ajax!="":
            obj = Num.objects.all().last()
            conname = obj.finame
           
            obj1 = Csv.objects.get(name=conname)
            csv = obj1.file_csv
            op = str(csv)
            final = media+op
            read = pd.read_csv(final)
            read.sort_values("mobile", inplace = True)
            read.drop_duplicates(subset ="mobile",keep ='first', inplace = True) 
       
            for i in read['mobile']:
                li.append(i)
                k+=1
            obj2 = Num.objects.all().last()
            obj3=Report.objects.all().filter(conname=obj2.finame,date__range=["2021-03-11","2021-03-12"])
            for i in obj3:
                if i.status=="success":
                    j+=1
                if i.status=="fail":
                    l+=1
                m=i.limit
                g+=1
            obj4 = Sim.objects.all().order_by('-id')[:32][::-1]
            for p in obj4:
                if n <= 7:
                    l1.append(p.pin)
                elif n <= 15:
                    l2.append(p.pin)
                elif n <= 23:
                    l3.append(p.pin)
                elif n <= 31:
                    l4.append(p.pin)
                n += 1
           
            a=g/k
            a*=100
            
            ob=Spin.objects.all().last()
            sent=ob.sim
            if sent=="A":
                z=1
            if sent=="B":
                z=2
            if sent=="C":
                z=3
            if sent=="D":
                z=4
            if sent=="E":
                z=5
            if sent=="F":
                z=6
            if sent=="G":
                z=7
            if sent=="H":
                z=8
            html_response = render_to_string(
            'outbox/ajaxoutbox.html', context={'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4,'k':k,'j':j,'l':l,'n':n,'m':m,'g':g,'a':a,'z':z})
            return HttpResponse(html_response, status=200)
        else:
            l = 1
            obj = Sim.objects.all().order_by('-id')[:32][::-1]
            for i in obj:
                if l <= 8:
                    l1.append(i.pin)
                elif l <= 16:
                    l2.append(i.pin)
                elif l <= 24:
                    l3.append(i.pin)
                elif l <= 32:
                    l4.append(i.pin)
                l += 1
            return render(request, 'outbox/outbox.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4})
    elif op.types=="16x8":
            obj4 = Sim.objects.all().order_by('-id')[:128][::-1]
            for i in obj4:
                if n <= 8:
                    l1.append(i.pin)
                elif n <= 16:
                    l2.append(i.pin)
                elif n <= 24:
                    l3.append(i.pin)
                elif n <= 32:
                    l4.append(i.pin)
                elif n <= 40:
                    l5.append(i.pin)
                elif n <= 48:
                    l6.append(i.pin)
                elif n <= 56:
                    l7.append(i.pin)
                elif n <= 64:
                    l8.append(i.pin)
                elif n <= 72:
                    l9.append(i.pin)
                elif n <= 80:
                    l10.append(i.pin)
                elif n <= 88:
                    l11.append(i.pin)
                elif n <= 96:
                    l12.append(i.pin)
                elif n <= 104:
                    l13.append(i.pin)
                elif n <= 112:
                    l14.append(i.pin)
                elif n <= 120:
                    l15.append(i.pin)
                elif n <= 128:
                    l16.append(i.pin)
                n += 1
            return render(request, 'outbox/outbox2.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
    elif op.types=="16x32":
            obj4 = Sim.objects.all().order_by('-id')[:512][::-1]
            for i in obj4:
                if n <= 32:
                    l1.append(i.pin)
                elif n <= 64:
                    l2.append(i.pin)
                elif n <= 96:
                    l3.append(i.pin)
                elif n <= 128:
                    l4.append(i.pin)
                elif n <= 160:
                    l5.append(i.pin)
                elif n <= 192:
                    l6.append(i.pin)
                elif n <= 224:
                    l7.append(i.pin)
                elif n <= 256:
                    l8.append(i.pin)
                elif n <= 288:
                    l9.append(i.pin)
                elif n <= 320:
                    l10.append(i.pin)
                elif n <= 352:
                    l11.append(i.pin)
                elif n <= 384:
                    l12.append(i.pin)
                elif n <= 416:
                    l13.append(i.pin)
                elif n <= 448:
                    l14.append(i.pin)
                elif n <= 480:
                    l15.append(i.pin)
                elif n <= 512:
                    l16.append(i.pin)
                n += 1
            return render(request, 'outbox/outbox3.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})
    elif op.types=="16x64":
            obj4 = Sim.objects.all().order_by('-id')[:1024][::-1]
            for i in obj4:
                if n <= 64:
                    l1.append(i.pin)
                elif n <= 128:
                    l2.append(i.pin)
                elif n <= 192:
                    l3.append(i.pin)
                elif n <= 256:
                    l4.append(i.pin)
                elif n <= 320:
                    l5.append(i.pin)
                elif n <= 384:
                    l6.append(i.pin)
                elif n <= 448:
                    l7.append(i.pin)
                elif n <= 512:
                    l8.append(i.pin)
                elif n <= 576:
                    l9.append(i.pin)
                elif n <= 640:
                    l10.append(i.pin)
                elif n <= 704:
                    l11.append(i.pin)
                elif n <= 768:
                    l12.append(i.pin)
                elif n <= 832:
                    l13.append(i.pin)
                elif n <= 896:
                    l14.append(i.pin)
                elif n <= 960:
                    l15.append(i.pin)
                elif n <= 1024:
                    l16.append(i.pin)
                n += 1
            return render(request, 'outbox/outbox.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n,'l5':l5,'l6': l6, 'l7': l7, 'l8': l8, 'l9': l9,'l10': l10, 'l11': l11, 'l12': l12, 'l13': l13,'l14': l14, 'l15': l15, 'l15': l15, 'l16': l16,})


def test(request):
    return render(request, 'index/index4.html')


def report(request):
    status = request.POST.get('status')
    date = request.POST.get('date')
    finame=request.POST.get('finame')
    i=0
    j=0
    k=0
    if status != "" and status != None and date != "" and date != None and finame != "" and finame != None:
        print(status, date,finame)
        obj6 = Report.objects.all().filter(status=status, date__contains=date,conname=finame)
        for n in obj6:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj6,'i':i,'j':j,'k':k})
    elif status != "" and status != None and date != "" and date != None:
        obj5 = Report.objects.all().filter(status=status, date__contains=date)
        for n in obj5:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj5,'i':i,'j':j,'k':k})
    elif status != "" and status != None  and finame != "" and finame != None:
        print(status, date,finame)
        obj4 = Report.objects.all().filter(status=status,conname=finame)
        for n in obj4:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj4,'i':i,'j':j,'k':k})
    elif status != None and status != "":
        print(status)
        obj3= Report.objects.all().filter(status=status)
        for n in obj3:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj3,'i':i,'j':j,'k':k})
    elif date != None and date != "":
        print(date)
        obj2 = Report.objects.all().filter(date__contains=date)
        for n in obj2:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj2,'i':i,'j':j,'k':k})
    elif finame != "" and finame != None:
        print(finame)
        obj1=Report.objects.all().filter(conname=finame)
        for n in obj1:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj1,'i':i,'j':j,'k':k})
    else:
        obj = Report.objects.all()
        for n in obj:
            i+=1
            if n.status=="success":
                j+=1
            elif n.status=="fail":
                k+=1
        return render(request, 'report.html', {'get': obj,'i':i,'j':j,'k':k})


def item(request):
    return render(request, 'outbox/outbox4.html')
