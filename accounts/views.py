from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
        else:
            return render(request,'accounts/login')
            redirect('acceuil')
    form=UserCreationForm()
    context={'form':form}
    return render(request, 'accounts/login.html',context)
