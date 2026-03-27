from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Note
        fields = ['title', 'content', 'color', 'pinned']