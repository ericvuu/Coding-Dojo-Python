from django.shortcuts import render, HttpResponse, redirect

def index(request):
  if 'key_name' in request.session:
    request.session['key_name'] += 1
    print('key exists!')
  else:
    request.session['key_name'] = 0
    print("key 'key_name' does NOT exist")

  return render(request, "index.html")

def destroy(request):
  del request.session['key_name']
  return redirect("/")

def plustwo(request):
  if 'key_name' in request.session:
    request.session['key_name'] += 1
  else:
    request.session['key_name'] = 1
  return redirect('/')
