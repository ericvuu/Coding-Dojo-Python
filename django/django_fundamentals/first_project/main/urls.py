from django.urls import path
from . import views

urlpatterns = [
  path('', views.blogs),
  path('blogs', views.index),
  path('root', views.root),
  path('blogs/new', views.new),
  path('blogs/create', views.create),
  path('blogs/<int:num>', views.show),
  path('blogs/<int:num>/edit', views.edit),
  path('blogs/<int:num>/delete', views.delete),
  path('blogs/json', views.printjson),
]
