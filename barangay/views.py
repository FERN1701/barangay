
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


def home(request):
    context = {
   
    }
    return render(request,'index.html',context)

