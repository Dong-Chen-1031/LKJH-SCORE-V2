from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'main.html',locals())

def test1(request):
    return HttpResponse('fff')
# Create your views here.
