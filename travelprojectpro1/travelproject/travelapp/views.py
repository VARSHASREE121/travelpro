from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import guide

# Create your views here.
def index(request):
    obj=place.objects.all()
    gobj=guide.objects.all()
    return render(request,'index.html',{'result':obj,'gresult':gobj})
"""def home(request):
    name="inmakes"
    return render(request,'home.html',{'obj':name})
def finalans(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    addition=x+y
    subtraction=x-y
    Multiplication=x*y
    division=x/y
    return render(request,'result.html',{'resadd':addition,'ressub':subtraction,'resmul':Multiplication,'resdiv':division})
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return render(request,'detail.html')
def thank(request):
    return render(request,'thanks.html')
def about(request):
    return render(request,'about.html')"""
