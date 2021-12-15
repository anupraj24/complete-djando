from django.http import request
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, redirect

 #logout here

def logout_view(request):
    logout(request)
    return render(request,'logout.html')

#login here

def login_view(request):
    next_page = request.GET.get("next")
    d = { 'is_login':False }

    if request.method== 'POST':
        username1 = request.POST['user']
        password1 = request.POST['pass']

        u = authenticate(username=username1,password=password1)

        if u:
            login(request,u)

            d = {'is_login':True}

            

            return render(request,'login.html',d)

        else:
            return render(request,'not creat account.html')

     
    return render(request,'login.html', d)

# signup
def signup_view(request):
   
    d = {"is_signup": False}
    if request.method=='POST':
        username1 = request.POST['user']
        password1 = request.POST['pass']
        firstname1 = request.POST['fn']
        lastname1 = request.POST['ln']

        u = User.objects.create_user(username=username1, password=password1, first_name=firstname1, last_name=lastname1)
        
        u.save()
       
        d = { 'is_signup': True}
        return render(request,'signup.html',d)
		

    return render(request,'signup.html',d)