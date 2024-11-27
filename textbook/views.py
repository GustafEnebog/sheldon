from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Unit, Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required


class UnitListView(generic.ListView):
    queryset = Unit.objects.filter(status_unit=1)
    template_name = "textbook/index.html"
    context_object_name = "unit_list"


def unit_detail(request, unit_slug):
    unit = get_object_or_404(Unit.objects.filter(status_unit=1), unit_slug=unit_slug)
    if request.user.is_authenticated:
        # If logged in, display only the user's own notes
        notes = unit.unit_note.filter(user_id=request.user).order_by("-created_on")
    else:
        # If logged out, don't display any notes
        notes = []

    notes_form = NoteForm()

    if request.method == "POST" and request.user.is_authenticated:
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.unit_id = unit
            note.user_id = request.user
            note.save()
            messages.success(request, 'Note successfully saved!')
            # This redirects back to the unit details page
            return redirect('unit_detail', unit_slug=unit_slug)

    return render(request, "textbook/singel-unit-display.html", {
        "unit": unit,
        "notes": notes,
        "notes_form": notes_form,
        "unit_id": unit.unit_id,  # Pass the unit ID to the template
    })


def note_edit(request, unit_slug, note_id):
    """
    View to edit a note
    """
    unit = get_object_or_404(Unit.objects.filter(status_unit=1), unit_slug=unit_slug)
    note = get_object_or_404(Note, id=note_id)

    # Ensure the current user is the author of the note
    if note.user_id != request.user:
        return HttpResponseForbidden("You do not have permission to edit this note.")

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully!")
            return redirect('unit_detail', unit_slug=unit_slug)
    else:
        form = NoteForm(instance=note)

    return render(request, 'textbook/note_edit.html', {'form': form, 'note': note, 'unit': unit})


def note_delete(request, unit_slug, note_id):
    """
    View to delete a note
    """
    unit = get_object_or_404(Unit.objects.filter(status_unit=1), unit_slug=unit_slug)
    note = get_object_or_404(Note, pk=note_id)

    if note.user_id == request.user:
        note.delete()
        messages.success(request, 'Note deleted!')
    else:
        messages.error(request, 'You can only delete your own note!')

    return HttpResponseRedirect(reverse('unit_detail', args=[unit_slug]))


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


# Custom error pages
def custom_403(request, exception):
    return render(request, '403.html', status=403)

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def custom_405(request, exception):
    return render(request, '405.html', status=405)

def custom_500(request):
    return render(request, '500.html.html', status=500)
