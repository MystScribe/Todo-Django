from django import forms
from . models import TodoModel
import datetime
now = datetime.datetime.now()

class TodoCreationForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 49px; outline: 0;  '
    }))
    todolist = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Todo',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 19px; outline: 0;  '
    }))
    textarea = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Text',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 10px; outline: 0;  '
    }))
    Done = forms.BooleanField(required=False)
    created = forms.DateTimeField(initial=now, widget=forms.DateTimeInput(attrs={
        'placeholder': 'Created',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 10px; outline: 0;  '
    }))


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 49px; outline: 0;  '
            }),
            'todolist': forms.TextInput(attrs={
                'placeholder': 'Todo',
                'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 19px; outline: 0;  '
            }),
            'textarea': forms.Textarea(attrs={
                'placeholder': 'Text',
                'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 10px; outline: 0;  '
            }),
            'created': forms.TextInput(attrs={
                'placeholder': 'Created',
                'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 10px; outline: 0;  '
            }),
        }
