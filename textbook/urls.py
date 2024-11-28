from . import views
from django.urls import path

from django.conf import settings
from django.contrib import admin
from textbook import views
from textbook.views import custom_404


urlpatterns = [
    path('', views.UnitListView.as_view(), name='index'),
    path('<slug:unit_slug>/edit_note/<int:note_id>/', views.note_edit, name='note_edit'),
    path('<slug:unit_slug>/delete_note/<int:note_id>/', views.note_delete, name='note_delete'),
    path('profile/', views.profile, name='profile'),
    path('<slug:unit_slug>/', views.unit_detail, name="unit_detail")
]
