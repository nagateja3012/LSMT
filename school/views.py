from __future__ import unicode_literals
from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login as auth_login
from school.models import Dashboard,Profile
from datetime import date
import datetime
from datetime import timedelta, time, date
import csv, io
from django.shortcuts import render
from django.contrib import messages 

# Create your views here.

def home(request):
	return render(request,'index.html',locals())


def about(request):
	return render(request,'about.html',locals())


def contact(request):
	return render(request,'contact.html',locals())

def course(request):
	return render(request,'courses.html',locals())


def teacher(request):
	return render(request,'teacher.html',locals())

def report(request):
    board = Dashboard.objects.all()
    if request.method=="POST":
        value= request.POST['phone']
        total_listrec = []
        total_listpay = []      
        if value == "Telephone Bills":
            board = Dashboard.objects.filter(heads = value)            
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)            
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Loans":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Misllanious":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Salary":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Fee Collection":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Current Bill":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "suspense":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Rent":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Transportation":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Capitals":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
        elif  value == "Advances":     
            board = Dashboard.objects.filter(heads = value)
            total_recall = Dashboard.objects.filter(heads = value)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum = sum(total_listrec)
            total_payall = Dashboard.objects.filter(heads = value)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum = sum(total_listpay)
            diff_total = total_recsum - total_paysum
            return render(request,'report_detail.html',locals())
    return render(request,'reports.html',locals())


def gallery(request):
	return render(request,'gallery.html',locals())

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return HttpResponseRedirect('/')
		else:
			msg = "Invalid Credentials"
	return render(request,'login.html', locals())


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def dashboard(request):
    board = Dashboard.objects.all()
    total_listrec = []
    total_recall = Dashboard.objects.all()
    for i in total_recall:
        total_listrec.append(i.receviable)
        total_recsum = sum(total_listrec)
    total_listpay = []
    total_payall = Dashboard.objects.all()
    for j in total_payall:
        total_listpay.append(j.payment)
        total_paysum = sum(total_listpay)
        diff_total = total_recsum - total_paysum
    if request.method == "POST":
        details_form = Dashboard.objects.create(
    		heads = request.POST["heads"],
    		date = request.POST["date"],
    		expenses_details = request.POST["expenses_details"],
    		receviable = request.POST["receviable"],
    		payment = request.POST["payment"],
    		)
        details_form.save()
    if request.method=="GET":
        total_listrec = []
        total_listpay = []
        s_time = request.GET.get('select_month')
        if s_time == 'today':
            today = date.today()
            board_report= Dashboard.objects.filter(date__gte=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_listpay = []
            total_payall = Dashboard.objects.filter(date__gte=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'yesterday':
            today = datetime.datetime.now()
            yesterday = datetime.datetime.now() - timedelta(days=1)
            board_report= Dashboard.objects.filter(date__gte=yesterday).filter(date__lt=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=yesterday).filter(date__lt=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=yesterday).filter(date__lt=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_week':
            today = datetime.datetime.now()
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            board_report = Dashboard.objects.filter(date__gte=start_of_week).filter(date__lt=end_of_week).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=start_of_week).filter(date__lt=end_of_week)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=start_of_week).filter(date__lt=end_of_week)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_week':
            today = datetime.datetime.now()
            yesterday = today - timedelta(days=today.weekday())
            last_week = yesterday - timedelta(days=7)
            board_report = Dashboard.objects.filter(date__gte=last_week).filter(date__lt=yesterday).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=last_week).filter(date__lt=yesterday)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=last_week).filter(date__lt=yesterday)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_month':
            today = datetime.datetime.now()
            year = datetime.datetime.now().year
            month =  datetime.datetime.now().month
            yesterday = datetime.datetime.now() - timedelta(days=1)
            last_week = datetime.datetime.now() - timedelta(days=7)
            last_month = today.replace(day=29) - timedelta(days=29)
            ninty = datetime.datetime.now() - timedelta(days=90)
            onety = datetime.datetime.now() - timedelta(days=180)
            last_year = datetime.datetime.now() - timedelta(days=365)
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6) 
            first = today.replace(day=1) 
            lastMonth = first - datetime.timedelta(days=1) 
            second = lastMonth - timedelta(days=30)
            lastquarter = ninty - timedelta(days=90)
            lastyear = last_year - timedelta(days=365)
            board_report = Dashboard.objects.filter(date__gte=last_month).filter(date__lt=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=last_month).filter(date__lt=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=last_month).filter(date__lt=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_month':
            today = datetime.datetime.now()
            year = datetime.datetime.now().year
            month =  datetime.datetime.now().month
            yesterday = datetime.datetime.now() - timedelta(days=1)
            last_week = datetime.datetime.now() - timedelta(days=7)
            last_month = datetime.datetime.now() - timedelta(days=30)
            ninty = datetime.datetime.now() - timedelta(days=90)
            onety = datetime.datetime.now() - timedelta(days=180)
            last_year = datetime.datetime.now() - timedelta(days=365)
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6) 
            first = today.replace(day=1) 
            lastMonth = first - datetime.timedelta(days=1) 
            second = lastMonth - timedelta(days=30)
            lastquarter = ninty - timedelta(days=90)
            lastyear = last_year - timedelta(days=365)
            board_report = Dashboard.objects.filter(date__gte=second).filter(date__lt=lastMonth).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=second).filter(date__lt=lastMonth)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=second).filter(date__lt=lastMonth)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_quarter':
            today = datetime.datetime.now()
            ninty = today.replace(day=1)  - timedelta(days=60)
            board_report = Dashboard.objects.filter(date__gte=ninty).filter(date__lt=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=ninty).filter(date__lt=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=ninty).filter(date__lt=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_quarter':
            today = datetime.datetime.now()
            ninty = today.replace(day=1)  - timedelta(days=60)
            lastquarter = ninty - timedelta(days=90)
            board_report = Dashboard.objects.filter(date__gte=lastquarter).filter(date__lt=ninty).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=lastquarter).filter(date__lt=ninty)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=lastquarter).filter(date__lt=ninty)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_year':
            today = datetime.datetime.now()
            la = today.replace(day=30,month=6)
            ly = la - timedelta(days=365)
            th_yr = ly + timedelta(days=396)
            board_report = Dashboard.objects.filter(date__gte=ly).filter(date__lt=th_yr).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=ly).filter(date__lt=th_yr)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=ly).filter(date__lt=th_yr)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_year':
            today = datetime.datetime.now()
            ty = today.replace(day=31,month=7) - timedelta(days=366)
            lastyear = ty - timedelta(days=396)
            board_report = Dashboard.objects.filter(date__gte=lastyear).filter(date__lt=ty).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=lastyear).filter(date__lt=ty)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=lastyear).filter(date__lt=ty)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
    return render(request,'dashboard.html',locals())

def dashboard_report(request):
    if request.method=="GET":
        total_listrec = []
        total_listpay = []
        s_time = request.GET.get('select_month')
        if s_time == 'today':
            today = date.today()
            board_report= Dashboard.objects.filter(date__gte=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_listpay = []
            total_payall = Dashboard.objects.filter(date__gte=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'yesterday':
            today = datetime.datetime.now()
            yesterday = datetime.datetime.now() - timedelta(days=1)
            board_report= Dashboard.objects.filter(date__gte=yesterday).filter(date__lt=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=yesterday).filter(date__lt=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=yesterday).filter(date__lt=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_week':
            today = datetime.datetime.now()
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            board_report = Dashboard.objects.filter(date__gte=start_of_week).filter(date__lt=end_of_week).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=start_of_week).filter(date__lt=end_of_week)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=start_of_week).filter(date__lt=end_of_week)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_week':
            today = datetime.datetime.now()
            yesterday = today - timedelta(days=today.weekday())
            last_week = yesterday - timedelta(days=7)
            board_report = Dashboard.objects.filter(date__gte=last_week).filter(date__lt=yesterday).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=last_week).filter(date__lt=yesterday)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=last_week).filter(date__lt=yesterday)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_month':
            today = datetime.datetime.now()
            year = datetime.datetime.now().year
            month =  datetime.datetime.now().month
            yesterday = datetime.datetime.now() - timedelta(days=1)
            last_week = datetime.datetime.now() - timedelta(days=7)
            last_month = today.replace(day=29) - timedelta(days=29)
            ninty = datetime.datetime.now() - timedelta(days=90)
            onety = datetime.datetime.now() - timedelta(days=180)
            last_year = datetime.datetime.now() - timedelta(days=365)
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6) 
            first = today.replace(day=1) 
            lastMonth = first - datetime.timedelta(days=1) 
            second = lastMonth - timedelta(days=30)
            lastquarter = ninty - timedelta(days=90)
            lastyear = last_year - timedelta(days=365)
            board_report = Dashboard.objects.filter(date__gte=last_month).filter(date__lt=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=last_month).filter(date__lt=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=last_month).filter(date__lt=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_month':
            today = datetime.datetime.now()
            year = datetime.datetime.now().year
            month =  datetime.datetime.now().month
            yesterday = datetime.datetime.now() - timedelta(days=1)
            last_week = datetime.datetime.now() - timedelta(days=7)
            last_month = datetime.datetime.now() - timedelta(days=30)
            ninty = datetime.datetime.now() - timedelta(days=90)
            onety = datetime.datetime.now() - timedelta(days=180)
            last_year = datetime.datetime.now() - timedelta(days=365)
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6) 
            first = today.replace(day=1) 
            lastMonth = first - datetime.timedelta(days=1) 
            second = lastMonth - timedelta(days=30)
            lastquarter = ninty - timedelta(days=90)
            lastyear = last_year - timedelta(days=365)
            board_report = Dashboard.objects.filter(date__gte=second).filter(date__lt=lastMonth).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=second).filter(date__lt=lastMonth)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=second).filter(date__lt=lastMonth)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_quarter':
            today = datetime.datetime.now()
            ninty = today.replace(day=1)  - timedelta(days=60)
            board_report = Dashboard.objects.filter(date__gte=ninty).filter(date__lt=today).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=ninty).filter(date__lt=today)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=ninty).filter(date__lt=today)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_quarter':
            today = datetime.datetime.now()
            ninty = today.replace(day=1)  - timedelta(days=60)
            lastquarter = ninty - timedelta(days=90)
            board_report = Dashboard.objects.filter(date__gte=lastquarter).filter(date__lt=ninty).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=lastquarter).filter(date__lt=ninty)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=lastquarter).filter(date__lt=ninty)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'this_year':
            today = datetime.datetime.now()
            la = today.replace(day=30,month=6)
            ly = la - timedelta(days=365)
            th_yr = ly + timedelta(days=396)
            board_report = Dashboard.objects.filter(date__gte=ly).filter(date__lt=th_yr).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=ly).filter(date__lt=th_yr)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=ly).filter(date__lt=th_yr)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
        if s_time == 'last_year':
            today = datetime.datetime.now()
            ty = today.replace(day=31,month=7) - timedelta(days=366)
            lastyear = ty - timedelta(days=396)
            board_report = Dashboard.objects.filter(date__gte=lastyear).filter(date__lt=ty).order_by('-date')
            total_recall = Dashboard.objects.filter(date__gte=lastyear).filter(date__lt=ty)
            for i in total_recall:
                total_listrec.append(i.receviable)
                total_recsum_detail = sum(total_listrec)
            total_payall = Dashboard.objects.filter(date__gte=lastyear).filter(date__lt=ty)
            for j in total_payall:
                total_listpay.append(j.payment)
                total_paysum_detail = sum(total_listpay)
                diff_total_detail = total_recsum_detail - total_paysum_detail
            return render(request,'dashboard_reportdaily.html',locals())
    return render(request,'dashboard_reportdaily.html',locals())

def profile_upload(request):
    template = "profile_upload.html"
    data = Profile.objects.all()
    prompt = {
            'order': 'Order of the CSV should be name, email, address,phone, profile',
            'profiles': data    
          }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            name=column[0],
            email=column[1],
            address=column[2],
            phone=column[3],
            profile=column[4]
        )
    context = {}
    return render(request, template, context)

