from django.shortcuts import render, redirect
from .models import Dojo, Ninja
def index(request):

  context = {
    "all_dojos": Dojo.objects.all(),
    "ninjas": Ninja.objects.all(),
  }

  return render(request, 'index.html', context)

def new_dojo(request):
  name = request.POST['dojo_name']
  city = request.POST['dojo_city']
  state = request.POST['dojo_state']

  Dojo.objects.create(name=name, city=city, state=state)
  return redirect('/')


def new_ninja(request):
  my_dojo = Dojo.objects.get(id=request.POST['ninja_dojo'])
  first_name = request.POST['ninja_first_name']
  last_name = request.POST['ninja_last_name']

  Ninja.objects.create(dojo=my_dojo, first_name=first_name, last_name=last_name)
  return redirect('/')

def delete(request, clan):

  deleted_dojo = Dojo.objects.get(id=clan)
  deleted_dojo.delete()

  return redirect('/')
