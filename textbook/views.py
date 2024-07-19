from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Unit, Note
from .models import Syllabus
from .forms import NotesForm
from django.contrib.auth.models import User


class UnitListView(generic.ListView):
    queryset = Unit.objects.filter(status_unit=1)
    template_name = "textbook/index.html"
    context_object_name = "unit_list"


def unit_detail(request, unit_slug):
    """
    Display an individual :model:`unit.note`.
    **Context**
    ``unit``
        An instance of :model:`textbook.Unit`.
    **Template:**
    :template:`textbook/unit_detail.html`
    """
    queryset = Unit.objects.filter(status_unit=1)
    unit_detail = get_object_or_404(queryset, unit_slug=unit_slug)
    unit = get_object_or_404(queryset, unit_slug=unit_slug)
    # notes = unit.notes.all().order_by("-created_on")
    print("this is Unit in detail view = ",unit)
    note = unit.unit_note.all().order_by("-created_on")
    notes_form = NotesForm()
    if request.method == "POST":
        note_form = NotesForm(data=request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.unit_id = Unit.objects.get(unit_slug=unit_slug)
            note.user_id = User.objects.get(id=request.user.id)
            note.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Note Succesfully saved'
            )
    
    return render(request, 
        "textbook/singel-unit-display.html", 
        {
            "unit": unit, 
            "note": note,
            "unit_detail": unit_detail,
            "notes_form": notes_form,
        },
    )


def note_edit(request, unit_slug, note_id):
    """
    view to edit note
    """
    if request.method == "POST":

        queryset = Unit.objects.filter(status_unit=1)
        unit = get_object_or_404(queryset, unit_slug=unit_slug)
        note = get_object_or_404(Note, pk=note_id)
        note_form = NotesForm(data=request.POST, instance=note)

        if note_form.is_valid() and note.user == request.user:
            note = note_form.save(commit=False)
            note.unit = unit
            note.status_unit = False
            note.save()
            messages.add_message(request, messages.SUCCESS, 'Note Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating note!')

    return HttpResponseRedirect(reverse('unit_detail', args=[unit_slug]))

def note_delete(request, unit_slug, note_id):
    """
    view to delete note
    """
    queryset = Unit.objects.filter(status_unit=1)
    unit = get_object_or_404(queryset, unit_slug=unit_slug)
    note = get_object_or_404(Note, pk=note_id)

    if note.user_id == request.user:
        note.delete()
        messages.add_message(request, messages.SUCCESS, 'Note deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own note!')

    return HttpResponseRedirect(reverse('unit_detail', args=[unit_slug]))

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
