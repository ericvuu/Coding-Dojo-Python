from django.shortcuts import render, redirect
from .models import User, Book
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

    return redirect('/success')

def process_login(request):
  login_errors = User.objects.validate_login(request.POST)

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
          return redirect('/success')
        else:
          messages.error(request,"Invalid Email or Password")
          return redirect('/')

  messages.error(request,"Invalid Email or Password")
  return redirect('/')

def success(request):

  if "user_id" in request.session:
    context = {
      "user": User.objects.get(id=request.session['user_id']),
      "all_users": User.objects.all(),
      "all_books": Book.objects.all(),
    }
  return render(request, 'profile.html', context)

def log_out(request):
  del request.session['user_id']
  print("logged out")
  return redirect('/')


def add_book(request):
  book_description_errors = Book.objects.validate_book_info(request.POST)

  if len(book_description_errors) > 0:
    for error in book_description_errors:
      messages.error(request, book_description_errors[error])
    return redirect('/success')
  else:
    this_user = User.objects.get(id=request.session['user_id'])
    book_title = request.POST['add_book_title']
    book_description = request.POST['add_book_description']
    new_book = Book.objects.create(title=book_title, description=book_description, uploaded_by=this_user)
    new_book.save()
    this_user.liked_books.add(new_book)
    return redirect('/success')

def view_book(request, book_num):
  current_book = Book.objects.get(id=book_num)
  author_id = current_book.uploaded_by.id

  if author_id == request.session['user_id']:
    context = {
    "current_book": current_book,
    "user": User.objects.get(id=request.session['user_id']),
    "all_book": Book.objects.all(),
    }
    return render(request, 'user_book_view.html', context)
  else:
    context = {
     "current_book": Book.objects.get(id=book_num),
     "user": User.objects.get(id=request.session['user_id']),
     "all_book": Book.objects.all(),
    }

  return render(request, 'view_book.html', context)

def edit_book(request, book_num):
  book_edit_errors = Book.objects.validate_book_edit(request.POST)

  if len(book_edit_errors) > 0:
    for error in book_edit_errors:
      messages.error(request, book_edit_errors[error])
    book_num = book_num
    return redirect(f'/books/{book_num}')
  else:
    this_book = Book.objects.get(id=book_num)
    this_book.title = request.POST['edit_book_title']
    this_book.description = request.POST['edit_book_description']
    this_book.save()
    book_num = book_num
    return redirect('/success')

def delete(request, book_num):
  this_book = Book.objects.get(id=book_num)
  this_book.delete()
  return redirect('/success')

def like_book(request, book_num):
  this_book = Book.objects.get(id=book_num)
  current_user = User.objects.get(id=request.session['user_id'])
  current_user.liked_books.add(this_book)
  current_user.save()
  return redirect('/success')

def remove_like_book(request, book_num):
  this_book = Book.objects.get(id=book_num)
  current_user = User.objects.get(id=request.session['user_id'])
  current_user.liked_books.remove(this_book)
  current_user.save()
  return redirect('/success')

#helper functions
#---------------------------------------------
# def checklogin():
#   if "user_id" in request.session:
#       print('user is signed in')
#   else:
#     print('not signed in')
#     return redirect('/')
