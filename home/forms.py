from django import forms
from .models import ToDo


class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    create = forms.DateField()


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'body','create']
