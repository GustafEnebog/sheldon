"""
URL configuration for sheldon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from textbook.views import textbook
#DELETE: we do no longer need this: from textbook import views as textbook_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", include("textbook.urls"), name="textbook-urls"),  #DELETE change this: path('textbook/', textbook_views.my_textbook, name='textbook'),   
]
