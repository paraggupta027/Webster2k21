from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User

#Auth and messages
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from uuid import uuid4

def home(request):
    return render(request,'home/index.html')

def signup(request):
    return render(request,'home/signup.html')

def signuphandle(request):

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        email = request.POST.get('email',"")
        password = request.POST.get('password',"")
        cpassword = request.POST.get('cpassword',"")

        if password != cpassword:
            print("Password did not match")
            return redirect('home')

        all_users = User.objects.all()

        for user in all_users:
            if user.email == email:
                print("Email already taken")
                return redirect('home')

        if password==cpassword:
            user = User.objects.create_user(fname,email,password)
            user.first_name = fname
            user.last_name = lname
            user.save()
    
        return render(request,'home/index.html')
