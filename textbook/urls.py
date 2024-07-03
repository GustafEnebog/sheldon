from . import views
from django.urls import path
#from django.urls import path
# from . import views


urlpatterns = [
    path('', views.UnitListView.as_view(), name='UnitContent'), # UnitContent is a view
    path('<slug:unit_slug>/', views.unit_detail, name="unit_detail"),
]
