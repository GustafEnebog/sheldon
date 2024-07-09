from .models import UserProgress
from django import forms


class NotesForm(forms.ModelForm):
    class Meta:
        model = UserProgress
        fields = ('user_notes')