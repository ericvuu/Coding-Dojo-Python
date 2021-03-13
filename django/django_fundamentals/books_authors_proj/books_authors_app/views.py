from django.shortcuts import render, redirect
from .models import Book, Author

# renders page functions

def books_home(request):

  context = {
    "all_books": Book.objects.all(),
    "all_authors": Author.objects.all(),
    }

  return render(request, 'books_home.html', context)

def view_book(request,book_num):

  context = {
    "all_books": Book.objects.all(),
    "all_authors": Author.objects.all(),
    "book_identification": Book.objects.get(id=book_num),
    }

  return render(request, 'view_book.html', context, book_num)

def authors_home(request):

  context = {
    "all_books": Book.objects.all(),
    "all_authors": Author.objects.all(),
    }

  return render(request, 'authors_home.html', context)

def view_author(request,auth_num):

  context = {
    "all_books": Book.objects.all(),
    "all_authors": Author.objects.all(),
    "author_identification": Author.objects.get(id=auth_num),
    }

  return render(request, 'view_author.html', context, auth_num)

# action functions

def add_new_book(request):
  new_book_title = request.POST['book_title']
  new_book_desc = request.POST['book_desc']

  Book.objects.create(title=new_book_title, desc=new_book_desc)

  return redirect('/')

def add_author_to_book(request, book_num):
  # stores the selected author's id from select menu in view_book.html
  current_author_id = request.POST['author_dropdown']
  # result of querying the author based upon the id
  current_author = Author.objects.get(id=current_author_id)
  # get current book based on id, book_num is routing variable
  current_book = Book.objects.get(id=book_num)
  # add author
  current_book.authors.add(current_author)
  # set book_num for redirection back to view_book page
  book_num = book_num
  return redirect(f'/books/{book_num}')

def add_new_author(request):
  new_author_first = request.POST['author_first_name']
  new_author_last = request.POST['author_last_name']
  new_author_notes = request.POST['author_notes']

  Author.objects.create(first_name=new_author_first, last_name=new_author_last, notes=new_author_notes)

  return redirect('/authors')

def add_book_to_author(request, auth_num):
  current_book_id = request.POST['book_dropdown']
  current_book = Book.objects.get(id=current_book_id)
  current_author = Author.objects.get(id=auth_num)
  current_author.books.add(current_book)
  auth_num = auth_num
  return redirect(f'/authors/{auth_num}')
