from . import views
from django.urls import path
#from django.urls import path
# from . import views


urlpatterns = [
    path('', views.Syllabus.as_view(), name='Syllabus'), # Syllabus is a view
    path('', views.Unit.as_view(), name='UnitContent'), # UnitContent is a view
]
