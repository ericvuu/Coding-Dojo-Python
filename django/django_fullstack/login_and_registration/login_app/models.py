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
    if len(postData['registration_password']) <= 0:
      errors['registration_password'] = "Please submit a password!"
    if postData['registration_password'] != postData['confirm_registration_password']:
      errors['confirm_registration_password'] = "Passwords do not match!"
    return errors

  def login_validation(self, postData):
    errors = {}
    if len(postData['login_email']) <= 0:
      errors['no_login_email'] = "Please submit your email"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(postData['login_email']):
      errors['login_email'] = "Invalid Email Address!"
    if len(postData['login_password']) <= 0:
      errors['login_password'] = "Please submit a password!"
    return errors

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = UserManager()
