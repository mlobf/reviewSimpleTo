from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',{'form':UserCreationForm(),'error':'That username has already been taken. Please choose other name'})
        else:
            return render(request, 'todo/signupuser.html',{'form':UserCreationForm(),'error':'Passwords did not match'})


def loginuser(request):
    if request.method =='GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                pass
            except:
                pass



def logoutuser(request):
    #We Shall Logout only if was a POST.
    #Some browsers in order to make things faster, the craw all GET links and load it. 
    # If logout was get, the user will be always login out without own will.
   if request.method =='POST':
       logout(request)
       return redirect('home')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')




