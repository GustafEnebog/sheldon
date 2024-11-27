from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['body']
        labels = {
            'body': '',  # This removes the label for the 'body' field
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Enter your note content here'}),  # Optional: Add a placeholder
        }
