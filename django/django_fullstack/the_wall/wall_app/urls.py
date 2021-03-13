from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('process_registration', views.process_registration),
  path('process_login', views.process_login),
  path('wall', views.success),
  path('logout', views.logout),
  path('post_message', views.post_message),
  path('post_comment', views.post_comment),
]
