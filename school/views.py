from __future__ import unicode_literals
from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login as auth_login
from school.models import Dashboard,BRSHDFC
# from school.forms import DocumentForm
from django.utils import timezone
import csv, io
from django.shortcuts import render
from django.contrib import messages 
# import dateparser
import datetime
from datetime import datetime,date, time, timedelta 
from dateutil import parser
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from kidzee.utils import render_to_pdf
from dateutil.relativedelta import relativedelta 
import sys
import xlwt
from importlib import reload
reload(sys)

# Create your views here.

# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()            
#     else:
#         form = DocumentForm()
#     return render(request, 'testdata.html', {
#         'form': form
#     })

class GeneratePdf(View):
    def get(self, request,slug, *args, **kwargs):
        template = get_template('pdf_download.html')
        today = date.today()
        start_of_yr = today.replace(day =1, month=4)
        end_of_yr = start_of_yr + relativedelta(months=11,days=31) - timedelta(days=1)
        board = Dashboard.objects.filter(expenses_details=slug, date__gte=start_of_yr, date__lte=end_of_yr)
        b = Dashboard.objects.values('expenses_details').distinct()
        total_listrec = []
        total_listpay = []
        total_recall = Dashboard.objects.filter(expenses_details=slug, date__gte=start_of_yr, date__lte=end_of_yr)
        for i in total_recall:
            total_listrec.append(i.receviable)
            total_recsum = sum(total_listrec)
            total_r = sum(total_listrec)
        total_payall = Dashboard.objects.filter(expenses_details=slug, date__gte=start_of_yr, date__lte=end_of_yr)
        for j in total_payall:
            total_listpay.append(j.payment)
            total_paysum = sum(total_listpay)
            total_p = sum(total_listpay)
            # diff_total = total_recsum - total_paysum
        if total_recsum >  total_paysum:
            tr = total_recsum - total_paysum
            total_paysum = total_paysum + tr
            # return HttpResponse("tr {{tr}}")
            tp = 0.0
            total_sum = total_paysum

        elif total_paysum > total_recsum:
            tp = total_paysum - total_recsum
            total_recsum = total_recsum + tp
            tr = 0.0
            total_sum = total_recsum
        context = {
             'board': board,
             'total_sum': total_sum,
             'total_recsum': total_recsum,
             'total_paysum':total_paysum,
             'total_r':total_r,
             'total_p':total_p,
             'tp': tp,
             'tr': tr,
             'start_of_yr': start_of_yr,
             'end_of_yr':end_of_yr
        }
        html = template.render(context)
        pdf = render_to_pdf("pdf_download.html",context)
        if pdf:
            response = HttpResponse(pdf,content_type = "application/pdf")
            filename = board[0].expenses_details+".pdf"
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")

class GeneratePdf_date(View):
    def get(self, request,slug, slug1, slug2, *args, **kwargs):
        template = get_template('pdf_download_date.html')
        board = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
        # return HttpResponse(board)
        total_listrec = []
        total_listpay = []
        total_recall = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
        for i in total_recall:
            total_listrec.append(i.receviable)
            total_recsum = sum(total_listrec)
            total_r = sum(total_listrec)
        total_payall = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
        for j in total_payall:
            total_listpay.append(j.payment)
            total_paysum = sum(total_listpay)
            total_p = sum(total_listpay)
            # diff_total = total_recsum - total_paysum
        if total_recsum >  total_paysum:
            tr = total_recsum - total_paysum
            total_paysum = total_paysum + tr
            # return HttpResponse("tr {{tr}}")
            tp = 0.0
            total_sum = total_paysum

        elif total_paysum > total_recsum:
            tp = total_paysum - total_recsum
            total_recsum = total_recsum + tp
            tr = 0.0
            total_sum = total_recsum
        context = {
            'board': board,
            'slug1':slug1,
            'slug2':slug2,
            'total_sum': total_sum,
            'total_recsum': total_recsum,
             'total_paysum':total_paysum,
             'total_r':total_r,
             'total_p':total_p,
             'tp': tp,
             'tr': tr,

        }
        html = template.render(context)
        pdf = render_to_pdf("pdf_download_date.html",context)
        if pdf:
            response = HttpResponse(pdf,content_type = "application/pdf")
            filename = slug+"_"+slug1+"_"+slug2+".pdf"
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")

def excel_download(request,slug):
    today = date.today()
    start_of_yr = today.replace(day =1, month=4)
    end_of_yr = start_of_yr + relativedelta(months=11,days=31) - timedelta(days=1)
    board = Dashboard.objects.filter(expenses_details=slug,date__gte=start_of_yr, date__lte=end_of_yr)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users', cell_overwrite_ok=True)
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_date= xlwt.XFStyle()
    font_date.num_format_str = 'D-MMM-YY'
    columns = ['date','expenses_details','description','heads','receviable','payment']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    # x = datetime.strptime(date, "%d/%m/%Y")
    rows = Dashboard.objects.filter(expenses_details=slug,date__gte=start_of_yr, date__lte=end_of_yr).values_list('date', 'expenses_details', 'description', 'heads', 'receviable', 'payment')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            ws.write(row_num, 0, row[0], font_date)
    wb.save(response)
    return response
    

def excel_download_date(request,slug,slug1,slug2,*args, **kwargs):
    today = date.today()
    board = Dashboard.objects.filter(expenses_details=slug,date__gte=slug1, date__lte=slug2)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users', cell_overwrite_ok=True)
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_date= xlwt.XFStyle()
    font_date.num_format_str = 'D-MM-YY'  #DD-MMM-YY
    style_vh_center = xlwt.easyxf('align: vert centre, horiz centre;''font: colour green, bold True;')
    # ws.write(0, 0, font_style)
    columns = ['date','expenses_details','description','heads','receviable','payment']
    for col_num in range(len(columns)):
       # ws.write_merge(0, 0,0, 10, "heading for excel \n hello world", style_vh_center)
        ws.write_merge(0,0,0, 10, "heading2 for excel \n hello world", style_vh_center)
    for col_num in range(len(columns)):
        row_num = 2     
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()    
    rows = Dashboard.objects.filter(expenses_details=slug,date__gte=slug1, date__lte=slug2).values_list('date', 'expenses_details', 'description', 'heads', 'receviable', 'payment')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            ws.write(row_num, 0, row[0], font_date)
    
    wb.save(response)
    return response

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


def layer(request):
    board = Dashboard.objects.values('expenses_details').distinct().order_by('expenses_details')
    return render(request,'layer.html',locals())


def data_upload(request):
    template = "data_upload.html"
    board_all = Dashboard.objects.all()
    prompt = {
            'order': 'Order of the CSV should be date, expenses_details, receviable,payment',
            'Dashboard': board_all    
          }
    if request.method == "GET":
        return render(request, template, prompt)
    if request.method == "POST":
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            x = column[0]
            s = parser.parse(x)
            dt = datetime.date(s)
            month = dt.month
            year = dt.year
            if column[2] == "" or column[2] == "0.0" or column[2] == " ":
                c2 = float(0.0)
            else:
                c2 = float(column[2])
            if column[3] == "" or column[3] == "0.0" or column[3] == " ":
                c3 = float(0.0)
            else:
                c3 = float(column[3].replace(",", ""))
            _, created = Dashboard.objects.update_or_create(
                date= dt,
                expenses_details=column[1],
                receviable=c2,
                payment=c3,
                date_month = month,
                date_year = year,
            )
        fs = FileSystemStorage(location="media/Dashboard")
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.url(filename)

        context = {}
        return render(request, template, context)


def hdfc_upload(request):
    template = "hdfc.html"
    board_all = BRSHDFC.objects.all()
    prompt = {
            'order': 'Order of the CSV should be date, Narration, Withdrawal,Deposit,LedgerDetails',
            'Dashboard': board_all    
          }
    if request.method == "GET":
        return render(request, template, prompt)
    if request.method == "POST":
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            x = column[0]
            s = parser.parse(x)
            dt = datetime.date(s)
            month = dt.month
            year = dt.year
            
            if column[2] == "" or column[2] == "0.0" or column[2] == " ":
                c2 = float(0.0)
            else:
                c2 = float(column[2])
            if column[3] == "" or column[3] == "0.0" or column[3] == " ":
                c3 = float(0.0)
            else:
                c3 = float(column[3].replace(",", ""))
            _, created = BRSHDFC.objects.update_or_create(
                date= dt,
                Narration=column[1],
                Withdrawal=c2,
                Deposit=c3,
                LedgerDetails=column[4],
                date_month = month,
                date_year = year,
            )
        fs = FileSystemStorage(location="media/HDFC")
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.url(filename)

        context = {}
        return render(request, template, context)


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
    current_year = datetime.now().year
    board = Dashboard.objects.all()
    total_listrec = []
    total_recsum = 0
    total_paysum = 0
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
        x = datetime.strptime(request.POST["date"], "%Y-%m-%d")
        recValue = float(0.0)
        PayValue = float(0.0)
        recValue = request.POST["receviable"]
        PayValue  = request.POST["payment"]
        if recValue == "" or recValue == "0.0":
            recValue = float(0.0)
        if PayValue == "" or PayValue == "0.0":
            PayValue = float(0.0)
        details_form = Dashboard.objects.create(
            heads = request.POST["heads"],
            date = request.POST["date"],
            expenses_details = request.POST["expenses_details"],
            receviable =recValue,
            payment =PayValue,
            date_month = x.month,
            date_year = x.year,
            )
        details_form.save()
    return render(request,'dashboard.html',locals())     


def layerdetail(request,slug):
    current_year = datetime.now().year
    today = date.today()
    start_of_yr = today.replace(day = 1, month=4)
    end_of_yr = start_of_yr + relativedelta(months=11,days=31) - timedelta(days=1)
    # return HttpResponse(end_of_yr)
    total_listrec = []
    total_listpay = []
    board = Dashboard.objects.filter(expenses_details=slug, date__gte=start_of_yr, date__lte=end_of_yr)
    total_recall = Dashboard.objects.filter(expenses_details=slug, date__gte=start_of_yr, date__lte=end_of_yr)
    try:
        for i in total_recall:
            total_listrec.append(i.receviable)
            total_recsum = sum(total_listrec)
            total_r = sum(total_listrec)
        total_payall = Dashboard.objects.filter(expenses_details=slug, date__gte=start_of_yr, date__lte=end_of_yr)
        for j in total_payall:
            total_listpay.append(j.payment)
            total_paysum = sum(total_listpay)
            total_p = sum(total_listpay)
            # diff_total = total_recsum - total_paysum
        if total_recsum >  total_paysum:
            tr = total_recsum - total_paysum
            total_paysum = total_paysum + tr
            # return HttpResponse("tr {{tr}}")
            # tp = 0.0
            total_sum = total_paysum

        elif total_paysum > total_recsum:
            tp = total_paysum - total_recsum
            total_recsum = total_recsum + tp
            # tr = 0.0
            total_sum = total_recsum
            # return HttpResponse("tp",tp)

        # start_date = ""
        # end_date = ""
        if request.method == "POST":
            start_date = request.POST["start_date"]
            end_date = request.POST["end_date"]
            # return HttpResponse(start_date)
            return HttpResponseRedirect("/layer-detail-date/"+slug+"/"+start_date+"/"+end_date+"/")
    except:
        return HttpResponse("no records")  
    return render(request,'layer_detail.html',locals())

def layerdetail_date(request,slug,slug1,slug2):
    board = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
    # return HttpResponse(board)

    total_listrec = []
    total_listpay = []
    total_recsum = 0
    total_paysum = 0
    total_recall = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
    for i in total_recall:
        total_listrec.append(i.receviable)
        total_recsum = sum(total_listrec)
        total_r = sum(total_listrec)
    total_payall = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
    for j in total_payall:
        total_listpay.append(j.payment)
        total_paysum = sum(total_listpay)
        total_p = sum(total_listpay)
        # diff_total = total_recsum - total_paysum
    if total_recsum >  total_paysum:
        tr = total_recsum - total_paysum
        total_paysum = total_paysum + tr
        # return HttpResponse("tr {{tr}}")
        # tp = 0.0
        total_sum = total_paysum

    elif total_paysum > total_recsum:
        tp = total_paysum - total_recsum
        total_recsum = total_recsum + tp
        # tr = 0.0
        total_sum = total_recsum
        # return HttpResponseRedirect("/down/"+slug+"/"+start_date+"/"+end_date+"/")

    return render(request,'layer_detail_date.html',locals())

def pdf_month(request,slug,slug1, slug2):
    current_year = datetime.now().year
    # slug1 =datetime.strptime(slug1, "%Y-%m-%d")
    # slug2 =datetime.strptime(slug2, "%Y-%m-%d")
    # return HttpResponse(slug1)
    board = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
    total_listrec = []
    total_listpay = []
    total_recall = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
    for i in total_recall:
        total_listrec.append(i.receviable)
        total_recsum = sum(total_listrec)
    total_payall = Dashboard.objects.filter(expenses_details=slug, date__gte=slug1, date__lte=slug2)
    for j in total_payall:
        total_listpay.append(j.payment)
        total_paysum = sum(total_listpay)
        diff_total = total_recsum - total_paysum
    # return HttpResponseRedirect('/pdf/'+slug+"/"+slug1+"/"+slug2+"/")
    return render(request,'pdf_month.html',locals())

def check_report(request):
    current_year = datetime.now().year
    if request.method == "POST":
        cur_year = request.POST['select_year']
        cur_month = request.POST['select_month']
        board_report = Dashboard.objects.filter(date_month=cur_month, date_year=cur_year)
        total_listrec = []
        total_recall = Dashboard.objects.filter(date_month=cur_month, date_year=cur_year)
        for i in total_recall:
            total_listrec.append(i.receviable)
            total_recsum_detail = sum(total_listrec)
        total_listpay = []
        total_payall = Dashboard.objects.filter(date_month=cur_month, date_year=cur_year)
        for j in total_payall:
            total_listpay.append(j.payment)
            total_paysum_detail = sum(total_listpay)
            diff_total_detail = total_recsum_detail - total_paysum_detail
    return render(request,'checkreport.html',locals())


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


def report(request):
    board = Dashboard.objects.all()
    try:
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
    except:
        pass
    return render(request,'reports.html',locals())
