from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def submitted(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comments_from_form = request.POST['comments']
    context = {
      "name" : name_from_form,
      "location" : location_from_form,
      "language" : language_from_form,
      "comments" : comments_from_form
    }

    return render(request, 'submitted.html', context)
