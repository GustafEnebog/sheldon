from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Unit # Earlier: Textbook but it should be a model
# DELETE do not need it anymore: from django.http import HttpResponse
from .models import Syllabus

# Create your views here.

# DELETE do not need it anymore: def my_textbook(request):
# DELETE do not need it anymore:     return HttpResponse("Hello, Textbook!")

class UnitListView(generic.ListView):
    # model = Unit # Earlier: Textbook but it should be a model
    queryset = Unit.objects.filter(status_unit=1)  # queryset = Unit.objects.all()
    template_name = "textbook/index.html"
    #paginate_by = 3
    context_object_name = "unit_list"


def unit_detail(request, unit_slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    **Template:**
    :template:`blog/post_detail.html`
    """
    # unit = Unit.objects.get(slug=unit_slug)
    # queryset = Post.objects.filter(status=1)
    # unit = Unit.objects.get(slug=unit_slug)
    unit = get_object_or_404(Unit, unit_slug=unit_slug)  # unit instead of queryset
    print("this is Unit in detail view = ",unit)
    return render(request, "textbook/singel-unit-display.html", {"unit": unit},)


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