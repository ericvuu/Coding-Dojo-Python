from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  desc = models.TextField(null = True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Title: {self.title}"

class Author(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  books = models.ManyToManyField(Book, related_name="authors")
  notes = models.TextField(null = True)

  def __repr__(self):
    return f"First Name: {self.first_name} Last Name: {self.last_name}"
