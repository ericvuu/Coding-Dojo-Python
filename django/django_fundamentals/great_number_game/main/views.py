from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
  random_number = (random.randint(1,100))
  request.session['comp_num'] = random_number
  request.session['times_wrong'] = 0
  return render(request, 'index.html')

def get_number(request):
  if request.method == "POST":
    user_num = int(request.POST["number-submitted"])
    print(f"User number is: {user_num}")
    print(f"random number is: {request.session['comp_num']}")

  if user_num > request.session['comp_num']:
    request.session['times_wrong'] += 1
    return redirect('/high')
  elif user_num < request.session['comp_num']:
    request.session['times_wrong'] += 1
    return redirect('/low')
  else:
    return redirect('/correct')

def go_high(request):
  return render(request, "too_high.html")

def go_low(request):
  return render(request, "too_low.html")

def go_correct(request):
  return render(request, "correct.html")
