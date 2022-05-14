from django.shortcuts import render
from django.http.response import HttpResponse

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