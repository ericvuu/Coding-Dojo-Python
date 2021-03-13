from django.db import models

class ShowManager(models.Manager):
  def add_form_validator(self, postData):
    errors = {}
    if len(postData['new_show_title']) < 2:
      errors['new_show_title'] = "Title must be at least 2 characters in length"
    if len(postData['new_show_network']) < 2:
      errors['new_show_network'] = "Network description but be at least 2 character in length."
    return errors

  def edit_form_validator(self,postData):
    errors = {}
    if len(postData['edit_show_title']) < 2:
      errors['edit_show_title'] = "Title must be at least 2 characters in length"
    if len(postData['edit_show_network']) < 2:
      errors['edit_show_network'] = "Network description but be at least 2 character in length."
    return errors

class Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=255)
  release_date = models.DateField()
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # override the objects property and have it reference ShowManager
  objects = ShowManager()

  def __repr__(self):
    return f"Title: {self.title} Network: {self.network}"
