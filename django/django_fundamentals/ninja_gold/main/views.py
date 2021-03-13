from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random

def index(request):
  # del request.session['user_log']
  # del request.session['user_money']
  if 'user_money' not in request.session:
    request.session['user_money'] = 0
  try:
    request.session['user_log']
  except KeyError:
    request.session['user_log'] = []
  return render(request,"index.html")

def process_coins(request):
  if request.POST['which_form'] == 'farm':
    random_number = random.randint(10,20)
    request.session['user_log'].append(f'Earned {random_number} golds from the Farm! ({strftime("%Y/%m/%d")} {strftime("%I:%M %p", localtime())})')
    request.session['user_money'] += random_number
  elif request.POST['which_form'] == 'cave':
    random_number = random.randint(5,10)
    request.session['user_log'].append(f'Earned {random_number} golds from the Cave! ({strftime("%Y/%m/%d")} {strftime("%I:%M %p", localtime())})')
    request.session['user_money'] += random_number
  elif request.POST['which_form'] == 'house':
    random_number = random.randint(2,5)
    request.session['user_log'].append(f'Earned {random_number} golds from the House! ({strftime("%Y/%m/%d")} {strftime("%I:%M %p", localtime())})')
    request.session['user_money'] += random_number
  else:
    random_number = random.randint(-50,50)
    request.session['user_money'] += random_number
    if random_number >= 0:
      request.session['user_log'].append(f'Earned {random_number} golds from the Casino! ({strftime("%Y/%m/%d")} {strftime("%I:%M %p", localtime())})')
    else:
      request.session['user_log'].append(f'Lost {random_number * -1} golds from the Casino! ({strftime("%Y/%m/%d")} {strftime("%I:%M %p", localtime())})')
  return redirect('/')
