from . import views
from django.urls import path

from django.conf import settings
# from django.conf.urls import handler403, handler404, handler405, handler500
from django.contrib import admin
from textbook import views
from textbook.views import custom_404

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.UnitListView.as_view(), name='index'),
    path('<slug:unit_slug>/edit_note/<int:note_id>/', views.note_edit, name='note_edit'),
    path('<slug:unit_slug>/delete_note/<int:note_id>/', views.note_delete, name='note_delete'),
    path('profile/', views.profile, name='profile'),
    path('<slug:unit_slug>/', views.unit_detail, name="unit_detail")
]

# Set the handlers to your custom view
handler403 = 'textbook.views.custom_403'
handler404 = 'textbook.views.custom_404'
handler405 = 'textbook.views.custom_405'
handler500 = 'textbook.views.custom_500'
