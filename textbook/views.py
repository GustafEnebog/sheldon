from django.shortcuts import render
from django.views import generic
from .models import Unit # Earlier: Textbook but it should be a model
# DELETE do not need it anymore: from django.http import HttpResponse
from .models import Syllabus

# Create your views here.

# DELETE do not need it anymore: def my_textbook(request):
# DELETE do not need it anymore:     return HttpResponse("Hello, Textbook!")

class Unit(generic.ListView):
    # model = Unit # Earlier: Textbook but it should be a model
    queryset = Unit.objects.filter(status_unit=1)  # queryset = Unit.objects.all()
    template_name = "textbook/index.html"
    # paginate_by = 6

class Syllabus(generic.ListView):
    # model = Unit # Earlier: Textbook but it should be a model
    queryset = Syllabus.objects.filter(status_syllabus=1) 
    template_name = "textbook/index.html"