from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls import handler404
from django.contrib import admin
from textbook import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.UnitListView.as_view(), name='index'),
    path('<slug:unit_slug>/edit_note/<int:note_id>/', views.note_edit, name='note_edit'),
    path('<slug:unit_slug>/delete_note/<int:note_id>/', views.note_delete, name='note_delete'),
    path('profile/', views.profile, name='profile'),
    path('<slug:unit_slug>/', views.unit_detail, name="unit_detail")  # This might be the catch all slug that hinders my 404 to show!
]

# Set the handler404 to your custom view
handler404 = 'textbook.views.custom_404'