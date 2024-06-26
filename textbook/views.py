from django.shortcuts import render, get_object_or_404
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
    #paginate_by = 3
    context_object_name = "unit_list"
    

class Syllabus(generic.ListView):
    # model = Unit # Earlier: Textbook but it should be a model
    queryset = Syllabus.objects.filter(status_syllabus=1)  # queryset = Unit.objects.all()
    template_name = "textbook/index.html"
    # paginate_by = 3
    context_object_name = "unit_list"


def unit_detail(request, slug):
    """
    Display an individual :model:`textbook.Unit`.

    **Context**

    ``unit``
        An instance of :model:`textbook.Unit`.

    **Template:**

    :template:`textbook/unit_detail.html`
    """

    queryset = Unit.objects.filter(status=1)
    unit = get_object_or_404(queryset, slug=unit_slug)

    return render(
        request,
        "textbook/unit_detail.html",
        {"unit": unit_slug}, # unit_slug> or slug> ?
    )


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, '500.html', status=500)


def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, '403.html', status=403)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, '405.html', status=405)