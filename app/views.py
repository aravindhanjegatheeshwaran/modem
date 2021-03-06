import threading
from datetime import datetime
import time
from django.http.response import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from app.check_port import check
from app.excuting import excuting
from .forms import CsvForm
from .models import Csv, Num, Numupdate, Report, Sim, Device, Spin
import pandas as pd
from prettytable import PrettyTable
import os
global COMPORT_NAME, sms

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media = os.path.join(BASE_DIR, 'media/')
logging.basicConfig(level=logging.DEBUG)


class message():
    def checks():
        x = check()
        result = {}
        for y in x:
            portname = str(y)
            if portname != None:
                result.setdefault('port', []).append(portname)
                sem = excuting(portName=portname)
                if sem.openComPort():
                    print("successfully open  port"+" "+portname)
                    smc = sem.checkCommunication()
                    print(smc)
                    if smc == logging.error:
                        print("Couldn't communicate with module")
                        result.setdefault('status', []).append("Not Ready")
                    else:
                        result.setdefault('status', []).append("Ready")
                        pin = sem.checkpin()
                        if pin:
                            result.setdefault('pin', []).append('Ready')
                            phone = sem.checkphone()
                            if phone:
                                for i in range(len(phone)):
                                    if (phone[i].isdigit()):
                                        num = num+phone[i]
                                result.setdefault('phone', []).append(num)
                            else:
                                result.setdefault('phone', []).append(
                                    'Check the sim')
                            imei = sem.checkimei()
                            result.setdefault('imei', []).append(imei)
                            signal = sem.checksignal()
                            if signal:
                                num = ""
                                for j in range(len(signal)):
                                    if (signal[j].isdigit()):
                                        num = num+signal[j]
                                result.setdefault('signal', []).append(num)
                            else:
                                result.setdefault('signal', []).append(
                                    'check the sim')
                        else:
                            result.setdefault('pin', []).append('Not Ready')
                        sem.closeComPort()
        return result

    def checks2():
        x = check()
        result = {}
        for y in x:
            portname = str(y)
            if portname != None:
                result.setdefault('port', []).append(portname)
                sem = excuting(portName=portname)
                if sem.openComPort():
                    print("successfully open  port"+" "+portname)
                    smc = sem.checkCommunication()
                    if smc == logging.error:
                        print("Couldn't communicate with module")
                        sem.closeComPort()
                        result.setdefault('status', []).append("Not Ready")
                    else:
                        result.setdefault('status', []).append("Ready")
                        al = 64
                        for i in range(8):
                            al += 1
                            msim = sem.mulsim(chr(al))
                            time.sleep(5)
                            if msim == logging.error:
                                print("couldn't set sim")
                                result.setdefault('sim', []).append(False)
                                sem.closeComPort()
                                break
                            else:
                                result.setdefault('sim', []).append(True)
                            pin = sem.checkpin()
                            if not pin:
                                result.setdefault('pin', []).append(False)
                            else:
                                result.setdefault('pin', []).append(True)
        return result

    def checks3():
        che=check()
        openport=[]
        for x in che:
            COMPORT_NAME = str(x)
            logging.basicConfig(level=logging.DEBUG)
            sms = excuting(portName=COMPORT_NAME)
            if sms.openComPort():
                print("successfully open  port"+" "+COMPORT_NAME)
                smc = sms.checkCommunication()
                if smc == logging.error:
                    print("Couldn't communicate with module")
                else:
                    if not sms.mulsim('A'):
                        logging.error("couldn't set sim")
                        sms.closeComPort()
                    else:
                        if not sms.checkpin():
                            logging.error("couldn't communicate with sim")
                            sms.closeComPort()
                        else:
                            openport.append(COMPORT_NAME)
                            sms.closeComPort()
        return openport


    def send(x,number, msg, name, limit):
        global get, al
        sms = excuting(portName=x)
        if sms.openComPort():
            if not sms.verbose():
                logging.error("couldn't set CMEE")
                sms.closeComPort()
            else:
                we = datetime.now()
                date = we.strftime("%Y-%m-%d")
                if name == "one":
                    get = sms.sendSms(number, msg)
                    if not get:
                        status = "fail"
                        Report.objects.create(num=number, msg=msg, date=date, status=status,pin="A",port=x)
                    else:
                        status = "success"
                        Report.objects.create(num=number, msg=msg, date=date, status=status,pin="A",port=x)
                        sms.closeComPort()
                        return get
                elif name == "multi":
                    n = 1
                    al = 65
                    for i in number:
                        print("numbr",x,i)
                        i = str(i)
                        limit=int(limit)
                        if n==limit:
                            n = 1
                            al = 66
                            sms.mulsim(chr(al))
                            pin=sms.checkpin()
                            if not pin:
                                sms.mulsim('A')
                            else:
                                time.sleep(10)
                                sim = chr(al)
                                Spin.objects.create(port=x, sim=sim)
                                get = sms.sendSms(i, msg)
                                if not get:
                                    status = "fail"
                                    Report.objects.create(num=i, msg=msg, date=date, status=status,pin=sim,port=x)
                                else:
                                    status = "success"
                                    Report.objects.create(num=i, msg=msg, date=date, status=status,pin=sim,port=x)
                        else:
                            sim = chr(al)
                            Spin.objects.create(port=x, sim=sim)
                            get = sms.sendSms(i, msg)
                            if not get:
                                status = "fail"
                                Report.objects.create(num=i, msg=msg, date=date, status=status,pin=sim,port=x)
                            else:
                                status = "success"
                                Report.objects.create(num=i, msg=msg, date=date, status=status,pin=sim,port=x)
                                n += 1
                    sms.closeComPort()
                    return get

    def thread(number, msg, name, limit):
        x_ls = message.checks3()
        thread_list = []
        x=len(number)//len(x_ls)
        i=0
        l3=[]
        while i<len(number):
            l3.append(number[i:i+x])
            i+=x
        for y,z in zip(x_ls,l3):
            thread = threading.Thread(target=message.send, args=(
                y,z, msg, name, limit), daemon=True)
            thread_list.append(thread)
        for thread in thread_list:
            thread.start()

    def read():
        global read
        port = message.open()
        portname = port
        if portname != None:
            sem = excuting(portName=portname)
            sem.openComPort()
            read = sem.readsms()
            if read == logging.error:
                return False
            else:
                return read


def index(request):
    res = request.POST.get('update')
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    n = 1
    if res == "Update":
        n = 1
        result = message.checks2()
        for i in result['pin']:
            Sim.objects.create(pin=i)
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
        return render(request, 'index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4, 'n': n})
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
    return render(request, 'index.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4})


def csvfile(request):
    if request.method == 'POST':
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
                print(i)        
                Numupdate.objects.create(name=csv,mobile=i)
            obj=Numupdate.objects.all().filter(name=csv)
            return render(request, 'contacts.html',{'get':obj})
    else:
        form = CsvForm()
        return render(request, 'contacts.html', {'form': form})


def manage(request):
    t = request.GET.get('type')
    count = request.GET.get('country')
    rate = request.GET.get('rate')

    return render(request, 'app_manage.html')


def device(request):
    global result
    report = ""
    disport = request.POST.get('disconnect_port')
    update = request.POST.get('update')
    if update != None and update!="":
        z = 1
        l1={}
        result = message.checks()
        for si in result['signal']:
            if si != "":
                si = int(float(si))
            if 50 <= si <= 100:
                report = "Excellent"
                l1.setdefault('report',[]).append(report)
            elif 20 <= si <= 50:
                report = "Good"
                l1.setdefault('report',[]).append(report)
            elif 2 <= si <= 20:
                report = "week"
                l1.setdefault('report',[]).append(report)
            elif si <= 1:
                report = "No signal"
                l1.setdefault('report',[]).append(report)
        port=result['port']
        status=result['status']
        pin=result['pin']
        phone=result['phone']
        imei=result['imei']
        signal=result['signal']
        report=l1['report']
        for i,j,k,l,m,n,o in zip(port,status,pin,phone,imei,signal,report):
            Device.objects.create(port=i,status=j,pin=k,phone=l,imei=m,signal=n,report=o)
        obj1=Device.objects.all().order_by('-id')[:4][::-1]
        return render(request, 'manage_device.html', {'get': obj1, 'n': z})
    else:
        obj=Device.objects.all().order_by('-id')[:4][::-1]
        return render(request, 'manage_device.html',{'get':obj})


def user(request):
    return render(request, 'manage_user.html')


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
    file1 = request.GET.get('file')
    limi = request.GET.get('limit1')
    finame = request.session['finame']
    ajax=request.GET.get('ajax')
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    if file1 != None:
        obj = Csv.objects.get(name=file1)
        csv = obj.file_csv
        op = str(csv)
        final = media+op
        read = pd.read_csv(final)
        j=0
        for i in read['mobile']:
            j+=1
        obj1=Report.objects.all().order_by('-id')[:j][::-1]
        obj2=Report.objects.all().filter(status='fail').order_by('-id')[:j][::-1]
        k=0
        for d in obj2:
            k+=1
            print(d.id,"thid",d.status)
        obj3=Report.objects.all().filter(status='success').order_by('-id')[:j][::-1]
        l=0
        for f in obj3:
            l+=1
            print(f.id,f.status)
        return render(request, 'sms_out_box1.html', {'num': l1,'get':obj1,'limit': limi,'fail':k,'suc':l})
    elif limit != None and send != None:
        name = "multi"
        li = []
        obj1 = Num.objects.all().filter(finame=finame).last()
        conname = obj1.finame
        msg = obj1.content
        print(msg)
        obj = Csv.objects.get(name=conname)
        csv = obj.file_csv
        op = str(csv)
        final = media+op
        read = pd.read_csv(final)
        for i in read['mobile']:
            if len(str(i))=='10':
                li.append(i)
        n = 1
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
        get = message.thread(li, msg, name, limit)
        request.session['finame'] = None
        return render(request, 'outbox.html', {'file': conname, 'limit': limit,'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4})
    elif ajax!=None and ajax!="":
        obj=Spin.objects.get().last()
        print(obj.sim)
        ajax="getlast()"
        return render(request,'outbox.html',{'ajax':ajax})
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
        return render(request, 'outbox.html', {'l1': l1, 'l2': l2, 'l3': l3, 'l4': l4})


def test(request):
    return render(request, 'sms_out_box1.html')


def report(request):
    status = request.POST.get('status')
    date = request.POST.get('date')
    if status != "" and status != None and date != "" and date != None:
        print(status, date)
        obj3 = Report.objects.all().filter(status=status, date=date)
        return render(request, 'report.html', {'get': obj3})
    elif status != None and status != "":
        print(status)
        obj1 = Report.objects.all().filter(status=status)
        return render(request, 'report.html', {'get': obj1})
    elif date != None and date != "":
        print(date)
        obj2 = Report.objects.all().filter(date=date)
        return render(request, 'report.html', {'get': obj2})
    else:
        obj = Report.objects.all()
        return render(request, 'report.html', {'get': obj})


def item(request):
    return render(request, 'sms_item.html')
