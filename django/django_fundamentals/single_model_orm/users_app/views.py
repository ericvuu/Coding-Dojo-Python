from django.shortcuts import render, redirect
from .models import User

def index(request):
  context = {
    "all_users": User.objects.all()
  }

  return render(request, "index.html", context)

def add_user(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email']
    age = request.POST['age']

  new_user = User.objects.create(first_name = first_name, last_name = last_name, email_address = email_address, age=age)
  new_user.save()

  return redirect('/')
