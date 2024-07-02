from . import views
from django.urls import path
#from django.urls import path
# from . import views


urlpatterns = [
    path('', views.Unit.as_view(), name='UnitContent'), # UnitContent is a view
]
