from django.urls import path
from . import views

app_name = "recipe_app"

urlpatterns = [
  path('', views.home, name="home"),
  path('sign_in_page', views.sign_in_page, name="sign_in_page"),
  path('registration_page', views.registration_page, name="registration_page"),
  path('register', views.register, name="register"),
  path('login', views.login, name="login"),
  path('dashboard', views.dashboard, name="dashboard"),
  path('findRecipes', views.findRecipes, name="findRecipes"),
  path('new_ingredient', views.new_ingredient,name="newIngredient"),
  path('add_ingredients_form', views.add_ingredients_form,name="add_ingredients_form"),
  path('send_email_update', views.send_email_update,name="send_email_update"),
  path('delete_ingredient', views.delete_ingredient, name="delete_ingrdient"),
  path('logout', views.logout,name="logout"),
  path('accountpage', views.settingspage),#this is to get to the settings page
  path('accountupdateinfo', views.accountupdateinfo),#this is to update the info
]
