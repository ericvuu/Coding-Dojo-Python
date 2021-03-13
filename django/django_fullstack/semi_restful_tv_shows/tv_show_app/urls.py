from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_redirect),
  path('shows', views.all_shows),
  path('shows/new', views.add_show),
  path('shows/new/process_add_show', views.process_add_show),
  path('shows/<int:show_id>', views.view_show),
  path('shows/<int:show_id>/edit', views.edit_show),
  path('shows/<int:show_id>/edit/process', views.process_edit_show),
  path('shows/<int:show_id>/destroy', views.remove_show),
]
