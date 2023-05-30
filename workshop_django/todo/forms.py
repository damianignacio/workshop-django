from django import forms
from .models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)
        if self.instance is not None:
            kwargs['initial'] = {
                "title": self.instance.title,
                "description": self.instance.description,
            }
        super().__init__(*args, **kwargs)

    def save(self):
        if self.instance is not None:
            self.instance.title = self.cleaned_data["title"]
            self.instance.description = self.cleaned_data["description"]
            self.instance.save()
        else:
            self.instance = Todo(**self.cleaned_data)
            self.instance.save()

        self.instance.refresh_from_db()

        return self.instance
