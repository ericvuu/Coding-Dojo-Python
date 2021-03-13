from django.db import models
import re

class UserManager(models.Manager):
  def validate_registration(self, postData):
    errors = {}
    if len(postData['registration_first_name']) < 3:
      errors['registration_first_name'] = "First name should be at least 3 characters"
    if len(postData['registration_last_name']) < 3:
      errors['registration_last_name'] = "Last name should be at least 3 characters"
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
  

  def validate_updateinfo(self, postData):
    errors = {}
    if len(postData['update_first_name']) < 3:
      errors['update_first_name'] = "First Name needs to be at least 3 Characters"
    if len(postData['update_last_name']) < 3:
      errors['update_last_name'] = "Last Name needs to be at least 3 Characters"
    
    check_email = User.objects.filter(email=postData['update_email'])
    if len(check_email) > 0:
      if postData['emailuse'] != postData['update_email']:
        errors['update_email'] = "This email is already registered"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(postData['update_email']):
      errors['update_email'] = "Invalid Email Address!"
    return errors


class IngredientManager(models.Manager):
  def validate_ingredient(self,postData):
    errors = {}
    if len(postData['newIngredient']) < 3:
      errors['newIngredient'] = "Ingredient name must be at least 3 characters!"
    if postData['purchase_date'] == '':
      errors['purchase_date'] = "Please provide a purchase date!"
    return errors

class Recipe(models.Model):
  api_id = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)
  userNotes = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return f"API ID: {self.api_id}"

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  favorite_recipes = models.ManyToManyField(Recipe, related_name="users_that_like")
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  
  objects = UserManager()

  def __repr__(self):
    return f"{self.first_name} {self.last_name}"

class Ingredient(models.Model):
  name = models.CharField(max_length=255)
  purchase_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  addedBy = models.ForeignKey(User, related_name="ingredients_added_to_database", on_delete=models.CASCADE)
  usersAssociated = models.ManyToManyField(User, related_name="ingredients")
  
  objects = IngredientManager()

  #associated_users = users which have this ingredient

  def __str__(self):
    return f"Ingredient Name:{self.name}"

