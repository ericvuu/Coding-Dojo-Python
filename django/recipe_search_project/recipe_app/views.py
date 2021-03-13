from django.shortcuts import render, redirect
from .models import User, Ingredient
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
import bcrypt, requests

from django.conf import settings
from django.core.mail import send_mail

def home(request):
  return render(request, 'home.html')

def sign_in_page(request):
  return render(request, 'sign_in.html')

def registration_page(request):
  return render(request, 'register.html')

def register(request):
  registration_errors = User.objects.validate_registration(request.POST)

  if len(registration_errors) > 0:
    for error in registration_errors:
      messages.error(request, registration_errors[error])
    return redirect('recipe_app:registration_page')
  else:
    first_name = request.POST['registration_first_name']
    last_name = request.POST['registration_last_name']
    email = request.POST['registration_email']
    password = request.POST['registration_password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)

    request.session['user_id'] = new_user.id

    return redirect('recipe_app:dashboard')

def login(request):
  login_errors = User.objects.validate_login(request.POST)

  if len(login_errors) > 0:
    for errors in login_errors:
      messages.error(request, login_errors[errors])
    return redirect('recipe_app:sign_in_page')
  else:
    current_login_email = request.POST['login_email']
    # get an array with the user object
    search_user = User.objects.filter(email=current_login_email)

    if search_user:
      # get the current user object
      this_user = search_user[0]

      if len(search_user) >= 0:

        if bcrypt.checkpw(request.POST['login_password'].encode(), this_user.password.encode()):
          request.session['user_id'] = this_user.id
          return redirect('recipe_app:dashboard')
        else:
          messages.error(request,"Invalid Email or Password")
          return redirect('recipe_app:sign_in_page')

  messages.error(request,"Invalid Email or Password")
  return redirect('recipe_app:sign_in_page')

def dashboard(request):
  logged_user = User.objects.get(id=request.session['user_id'])
  context = {
    "logged_user": logged_user,
  }
  return render(request, "dashboard.html", context)

def new_ingredient(request):
  errors = Ingredient.objects.validate_ingredient(request.POST)
  if len(errors) > 0:
    for key,value in errors.items():
      messages.error(request, value)
    return redirect("recipe_app:dashboard")
  else:
    logged_user = User.objects.get(id=request.session['user_id'])
    if len(Ingredient.objects.filter(name=request.POST['newIngredient'])) > 0:
      new_ingredient = Ingredient.objects.filter(name=request.POST['newIngredient'])[0]
    else:
      new_ingredient = Ingredient.objects.create(
        name=request.POST['newIngredient'],
        addedBy = logged_user,
        purchase_date=request.POST['purchase_date'],
      )

    logged_user.ingredients.add(new_ingredient)
    logged_user.save()
    htmlString = f"<tr ingredient_row='{new_ingredient.name}''><td>{new_ingredient.name}</td><td>{new_ingredient.purchase_date}</td><td><input class='form-check-input' type='checkbox' name='{new_ingredient.name}'></td><td><button class='btn btn-link' button_type='delete' button_name='{new_ingredient.name}'>Delete</button></td>"
    return HttpResponse(htmlString)

def delete_ingredient(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    logged_user.ingredients.remove(Ingredient.objects.get(name=request.POST['ingredient_name']))
    return HttpResponse("")

def findRecipes(request):
  # Alex's spoonacular apiKey=f0e942aff1534186a6f8307569a88964
  apiKey = "ea993de9a73c40789069a174c4ce5977"
  ingredients = "ingredients="
  logged_user = User.objects.get(id=request.session['user_id'])
  first = True
  for ingredient in logged_user.ingredients.all():
    if ingredient.name in request.POST:
      if first:
        ingredients = ingredients + f"{ingredient.name}"
        first = False
      else:
        ingredients = ingredients + f",+{ingredient.name}"

  url = f"https://api.spoonacular.com/recipes/findByIngredients/?apiKey={apiKey}&{ingredients}"
  url2 = f"https://api.spoonacular.com/recipes/findByIngredients/?apiKey={apiKey}&ingredients=milk"
  results = requests.get(url)
  jsonResults = results.json()

  return JsonResponse(jsonResults, safe=False)

def logout(request):
  request.session.clear()
  messages.success(request, "Successfully logged out - come back again soon!")
  return redirect('recipe_app:sign_in_page')

def add_ingredients_form(request):
  return render(request,"addIngredientsForm.html")

def send_email_update(request):
  logged_user = User.objects.get(id=request.session['user_id'])
  subject='test'
  message=f'Hi {logged_user.first_name}! This is a test!'
  email_from = settings.EMAIL_HOST_USER
  recipients = [logged_user.email,]
  msg_html=render_to_string('newsletter.html')
  send_mail(subject,message,email_from,recipients,html_message=msg_html)
  return redirect('recipe_app:dashboard')

def settingspage(request):#this is to get to the settings page
  context = {
    'user': User.objects.get(id=request.session['user_id']),
  }
  return render(request, "account_settings.html", context)

def accountupdateinfo(request):#this is to update the info
  update_errors = User.objects.validate_updateinfo(request.POST)
  if len(update_errors) > 0:
    for errors in update_errors:
      messages.error(request, update_errors[errors])
    return redirect('/accountpage')
  else:
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.first_name = request.POST['update_first_name']
    this_user.last_name = request.POST['update_last_name']
    this_user.email = request.POST['update_email']
    this_user.save()
    messages.success(request, "User info updated!")
    return redirect("/accountpage")
