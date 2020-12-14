from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# la fonction login
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        elif username == '':
            messages.info(request, 'Login vide!')
        elif password=='':
            messages.info(request,'mot de passe vide')
        else:
            messages.info(request,'Login ou mot de passe incorrect!')
    context={}
    return render(request,'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

