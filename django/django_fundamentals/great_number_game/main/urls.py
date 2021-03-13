from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('submit', views.get_number),
  path('high', views.go_high),
  path('low', views.go_low),
  path('correct', views.go_correct),
]
