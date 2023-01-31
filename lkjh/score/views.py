from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('fff')

def test1(request):
    return render(request,'main.html',locals())
# Create your views here.
