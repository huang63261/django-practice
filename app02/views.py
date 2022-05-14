from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.

def sayhi1(request):
    return HttpResponse("你好，歡迎光臨")

def sayhi2(request):
    return HttpResponse("你好，生日快樂")

def sayhi3(request):
    return HttpResponse("你好，新年快樂")

def sayhi4(request, myname):
    return HttpResponse(myname + "你好，歡迎光臨")

def sayhi5(request, myname):
    return HttpResponse(myname + "你好，生日快樂")

def sayhi6(request, myname):
    now = datetime.today
    return render(request, 'sayhi6.html', locals())
    # 將變數傳到模板。 locals()代表傳遞所有的區域變數
