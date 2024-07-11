from .models import Note
from django import forms


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('body',)