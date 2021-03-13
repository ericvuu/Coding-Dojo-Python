from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('process_registration', views.process_registration),
  path('process_login', views.process_login),
  path('success', views.success),
  path('log_out', views.log_out),
  path('add_book', views.add_book),
  path('books/<int:book_num>', views.view_book),
  path('edit_book/<int:book_num>', views.edit_book),
  path('delete/<int:book_num>', views.delete),
  path('like_book/<int:book_num>', views.like_book),
  path('remove_like_book/<int:book_num>', views.remove_like_book),
]
