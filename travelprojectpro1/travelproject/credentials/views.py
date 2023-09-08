from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        rpassword=request.POST['rpass']
        if password==rpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();    
                print("User Created") # terminal message shows
                return redirect('login')
        else:
            messages.info(request,"Password not matching")  
            print("password not matching") #terminal message shows
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')