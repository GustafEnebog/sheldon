from . import views
from django.urls import path
#from django.urls import path
# from . import views


urlpatterns = [
    path('', views.Unit.as_view(), name='UnitContent'), # UnitContent is a view
    path('<slug:unit_slug>/', views.unit_detail, name='unit_detail'), # unit_slug> or slug> ?
    path('', views.Syllabus.as_view(), name='Syllabus'), # Syllabus is a view
]
