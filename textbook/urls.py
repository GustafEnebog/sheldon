from . import views
from django.urls import path
#from django.urls import path
# from . import views


urlpatterns = [
    path('', views.UnitListView.as_view(), name='UnitContent'), # UnitContent is a view
    path('<slug:unit_slug>/', views.unit_detail, name="unit_detail"),
    path('<slug:unit_slug>/edit_note/<int:note_id>',
         views.note_edit, name='note_edit'),
    path('<slug:unit_slug>/delete_note/<int:note_id>',  # DELETE
         views.note_delete, name='note_delete'),  # DELETE
]

handler404 = 'textbook.views.handler404'
handler500 = 'textbook.views.handler500'
handler403 = 'textbook.views.handler403'
handler405 = 'textbook.views.handler405'