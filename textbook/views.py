from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Unit, Note
from .forms import NoteForm  # Make sure it's NoteForm, not NotesForm
from django.contrib.auth.decorators import login_required


class UnitListView(generic.ListView):
    queryset = Unit.objects.filter(status_unit=1)
    template_name = "textbook/index.html"
    context_object_name = "unit_list"


def unit_detail(request, unit_slug):
    unit = get_object_or_404(Unit.objects.filter(status_unit=1), unit_slug=unit_slug)
    notes = unit.unit_note.all().order_by("-created_on")
    
    # Use NoteForm here (not NotesForm)
    notes_form = NoteForm()

    if request.method == "POST":
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.unit_id = unit
            note.user_id = request.user
            note.save()
            messages.success(request, 'Note Successfully saved!')

    return render(request, "textbook/singel-unit-display.html", {
        "unit": unit,
        "notes": notes,
        "notes_form": notes_form,
    })


def note_edit(request, unit_slug, note_id):
    # Retrieve the note by its ID
    note = get_object_or_404(Note, id=note_id)
    
    # Ensure only the note's owner can edit it
    if note.user_id != request.user:
        return HttpResponseForbidden("You do not have permission to edit this note.")

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)  # Pre-populate form with existing note data
        if form.is_valid():
            form.save()  # Save the updated note
            return redirect('note_detail', note_id=note.id)  # Redirect to the note detail page after editing
    else:
        form = NoteForm(instance=note)  # Show the form with the existing note content

    # return render(request, 'note_edit.html', {'form': form, 'note': note, 'unit_slug': unit_slug})
    return render(request, 'textbook/note_edit.html', {'form': form, 'note': note, 'unit_slug': unit_slug})



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
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler405(request, exception):
    return render(request, '405.html', status=405)
