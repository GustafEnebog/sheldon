from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Unit, Note # Earlier: Textbook but it should be a model
# DELETE do not need it anymore: from django.http import HttpResponse
from .models import Syllabus # See if this one could be moved to from .models import Unit, Comment on row 5
from .forms import NotesForm
from django.contrib.auth.models import User

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
    
    #comments = post.comments.all().order_by("-created_on")
    #comment_count = post.comments.filter(approved=True).count()
    # unit = Unit.objects.get(slug=unit_slug)
    # queryset = Post.objects.filter(status=1)
    # unit = Unit.objects.get(slug=unit_slug)
    queryset = Unit.objects.filter(status_unit=1)
    unit_detail = get_object_or_404(queryset, unit_slug=unit_slug)  # Help from Sarah
    unit = get_object_or_404(queryset, unit_slug=unit_slug)  # unit instead of queryset
    print("this is Unit in detail view = ",unit)
    note = unit.unit_note.all().order_by("-created_on")
    #note_count = unit.unit_note.filter(approved=True).count()
    notes_form = NotesForm()
    # post = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        note_form = NotesForm(data=request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.unit_id = Unit.objects.get(unit_slug=unit_slug)  #CORRECT!
            note.user_id = User.objects.get(id=request.user.id)  #CORRECT!
            note.save()

            #Confirmation message, not yet working, also in base
            messages.add_message(
            request, messages.SUCCESS,
            'Note Succesfully save'
            )
            #END OF Confirmation message, not yet working, also in base

    #note_form = notes_form()
    
    return render(request, 
        "textbook/singel-unit-display.html", 
        {
            "unit": unit, 
            "note": note,
            "unit_detail": unit_detail,
            #"note_form": note_form,    THIS MIGHT BE SOMETHING TOO CHANGE!!!!
            "notes_form": notes_form,
        },
        #"note": note,
        #"note_count": notes_count,
        #"note_form": note_form,
    )


def note_edit(request, slug, note_id): # slug or unit_slug!? Here and further down in code in this view as well
    """
    view to edit note
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1) # Should maybe be unit to the right of =
        post = get_object_or_404(queryset, slug=slug) # Should maybe be unit to the left of =
        note = get_object_or_404(Note, pk=user_id) # Note tot he right of equal sign must refer to the model since capital N  CHANGE comment_id!!!
        note_form = NotesForm(data=request.POST, instance=note) # Plural since I have my forms.py in plural (notes) Same here as comment above. Is POST method or should it be changed ot UNIT?

        if note_form.is_valid() and note.author == request.user: # note.author or note.user_id!? REMEMBER TO CHANGE IN BUTTON IN singel-unit-display.html as well!
            note = note_form.save(commit=False)
            note.unit = unit # Should it be post or unit!?
            note.approved = False
            note.save()
            messages.add_message(request, messages.SUCCESS, 'Note Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating note!')

    return HttpResponseRedirect(reverse('unit_detail', args=[slug]))

# DELETE
def note_delete(request, slug, note_id):
    """
    view to delete note
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    note = get_object_or_404(Note, pk=user_id)   # CHANGE comment_id!!!

    if note.author == request.user:
        note.delete()
        messages.add_message(request, messages.SUCCESS, 'Note deleted!')  # What is add_message?
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own note!')   # What is add_message?

    return HttpResponseRedirect(reverse('unit_detail', args=[slug]))
# END OF DELETE

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