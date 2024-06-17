from django.shortcuts import render
from django.views import generic
from .models import Unit # Earlier: Textbook but it should be a model
# DELETE do not need it anymore: from django.http import HttpResponse

# Create your views here.

# DELETE do not need it anymore: def my_textbook(request):
# DELETE do not need it anymore:     return HttpResponse("Hello, Textbook!")

class UnitList(generic.ListView):
    # model = Unit # Earlier: Textbook but it should be a model
    queryset = Unit.objects.all()
    template_name = "unit_list.html"