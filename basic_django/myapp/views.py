from unicodedata import name
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"home.html",{"name":"good morning"})

def base(request):
    return render(request, 'base.html')


def result(request):
    print(request.method)

    val1=request.POST['num1']
    val2=request.POST['num2']

    res=int(val1)+int(val2)


    return render(request,"result.html",{"result":res})