from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):

    context= {

    }

    return render(request, 'accounts/dashboard.html', context)

def earn(request):
    return render(request, 'accounts/earn.html')


def withdraw(request):
    return render(request, 'accounts/withdraw.html')


def withdrawconfirm(request):
    return render(request, 'accounts/withdrawlconfirm.html')

