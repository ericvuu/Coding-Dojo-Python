from django.db import models
import re

class UserManager(models.Manager):
  def validate_registration(self, postData):
    errors = {}
    if len(postData['registration_first_name']) < 2:
      errors['registration_first_name'] = "First name should be at least 2 characters"
    if len(postData['registration_last_name']) < 2:
      errors['registration_last_name'] = "Last name should be at least 2 characters"
    # checks if there is an existing email
    check_email = User.objects.filter(email=postData['registration_email'])
    if len(check_email) > 0:
      errors['registration_email'] = "This email is already registered"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(postData['registration_email']):
      errors['registration_email'] = "Invalid Email Address!"
    if len(postData['registration_password']) < 7:
      errors['registration_password'] = "Password is too short! Needs to be at least 8 characters in length"
    if postData['registration_password'] != postData['confirm_registration_password']:
      errors['confirm_registration_password'] = "Passwords do not match!"
    return errors

  def validate_login(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(postData['login_email']) <= 0 and not EMAIL_REGEX.match(postData['login_email']) and len(postData['login_password']) <= 0:
      errors['login_error'] = "Invalid Email or Password"
    return errors

    # errors = {}
    # if len(postData['login_email']) <= 0:
    #   errors['no_login_email'] = "Please submit your email"
    # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    # if not EMAIL_REGEX.match(postData['login_email']):
    #   errors['login_email'] = "Invalid Email Address!"
    # if len(postData['login_password']) <= 0:
    #   errors['login_password'] = "Please submit a password!"
    # return errors

class BookManager(models.Manager):
  def validate_book_info(self, postData):
    errors = {}
    if len(postData['add_book_title']) < 6:
      errors['book_title'] = "The book title should be at least 5 characters"
    if len(postData['add_book_description']) <= 6:
      errors['book_description'] = "Please add a book description that is at least 5 characters long"
    return errors

  def validate_book_edit(self, postData):
    errors = {}
    if len(postData['edit_book_title']) < 6:
      errors['edit_book_title'] = "The book title should be at least 5 characters"
    if len(postData['edit_book_description']) <= 6:
      errors['edit_book_description'] = "Please add a book description that is at least 5 characters long"
    return errors


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  # books_uploaded = a list of books uploaded by a given user
  # liked_books = a list of books a given user likes

  objects = UserManager()

  def __repr__(self):
    return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    #  the user who uploaded a given book
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    # a list of users who like a given book
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

    def __repr__(self):
      return f"{self.title}"
