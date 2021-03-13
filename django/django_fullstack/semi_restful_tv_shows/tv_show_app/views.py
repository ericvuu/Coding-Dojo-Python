from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show

def main_redirect(request):
  return redirect('/shows')

def all_shows(request):

  context = {
    "all_shows": Show.objects.all(),
  }

  return render(request, 'all_shows.html', context)

def add_show(request):
  return render(request, 'add_show.html')

def process_add_show(request):

  errors = Show.objects.add_form_validator(request.POST)

  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/shows/new')
  else:
    new_show_title = request.POST['new_show_title']
    new_show_network = request.POST['new_show_network']
    new_show_release_date = request.POST['new_show_release_date']
    new_show_description = request.POST['new_show_description']

    new_show = Show.objects.create(title=new_show_title, network=new_show_network, release_date=new_show_release_date, description=new_show_description)
    new_show.save()

    show_id = new_show.id
    return redirect(f'/shows/{show_id}')

def view_show(request, show_id):

  context = {
    "current_show": Show.objects.get(id=show_id),
  }

  return render(request, 'view_show.html', context)

def edit_show(request, show_id):
  context = {
    "current_show": Show.objects.get(id=show_id),
  }
  return render(request, 'edit_show.html', context)

def process_edit_show(request, show_id):

  errors = Show.objects.edit_form_validator(request.POST)

  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return redirect(f'/shows/{show_id}/edit')
  else:
    current_show = Show.objects.get(id=show_id)
    new_title = request.POST['edit_show_title']
    new_network = request.POST['edit_show_network']
    new_release_date = request.POST['edit_show_release_date']
    new_description = request.POST['edit_show_description']

    current_show.title = new_title
    current_show.network = new_network
    current_show.release_date = new_release_date
    current_show.description = new_description
    current_show.save()
    return redirect('/shows')

def remove_show(request, show_id):
  get_deleted_show = Show.objects.get(id=show_id)
  get_deleted_show.delete()

  return redirect('/shows')
