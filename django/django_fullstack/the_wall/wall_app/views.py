from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

def index(request):
  return render(request, 'index.html')

def process_registration(request):
  registration_errors = User.objects.validate_registration(request.POST)

  if len(registration_errors) > 0:
    for error in registration_errors:
      messages.error(request, registration_errors[error])
    return redirect('/')
  else:
    first_name = request.POST['registration_first_name']
    last_name = request.POST['registration_last_name']
    email = request.POST['registration_email']
    password = request.POST['registration_password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)

    request.session['user_id'] = new_user.id

    return redirect('/wall')

def process_login(request):
  login_errors = User.objects.login_validation(request.POST)

  # check if errors
  if len(login_errors) > 0:
    for errors in login_errors:
      messages.error(request, login_errors[errors])
    return redirect('/')
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
          return redirect('/wall')
        else:
          messages.error(request,"Wrong Password")
          return redirect('/')

  messages.error(request,"Your email does not match our records.")
  return redirect('/')

def success(request):
  if 'user_id' in request.session:
    context = {
      "user": User.objects.get(id=request.session['user_id']),
      "all_users": User.objects.all(),
      "all_messages": Message.objects.all(),
      "all_comments": Comment.objects.all(),
    }
    return render(request, 'success.html', context)
  else:
    messages.error(request,"Access Restricted, Must be signed in!")
    return redirect('/')

def logout(request):
  del request.session['user_id']
  return redirect('/')

#  message and comment actions

def post_message(request):
  current_user = User.objects.get(id=request.session['user_id'])
  current_message = request.POST['post_message']
  add_message = Message.objects.create(context=current_message, user=current_user)
  add_message.save()
  # print(f'{current_user.first_name} said {current_message}')
  return redirect('/wall')

def post_comment(request):
  # get the current message id
  message_id = request.POST['message_id']
  # get current message with hidden form input value
  current_message = Message.objects.get(id=message_id)
  # get user id who made post
  user_message = current_message.user
  # get logged in person
  commenter = User.objects.get(id=request.session['user_id'])
  add_comment = request.POST['post_comment']
  new_comment = Comment.objects.create(context=add_comment, user=commenter, message=current_message)
  return redirect('/wall')
