from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse
# from app.models import Contact,logs
from django.contrib import messages

def home(request):
    return HttpResponse("hello")
