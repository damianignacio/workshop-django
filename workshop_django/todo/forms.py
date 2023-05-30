from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
