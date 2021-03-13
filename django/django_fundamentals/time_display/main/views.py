from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

def index(request):
  context = {
    "date": strftime("%b-%d-%Y"),
    "time": strftime("%I:%M %p", localtime()),
  }
  return render(request, "index.html", context)

def back(request):
  return redirect('/')
