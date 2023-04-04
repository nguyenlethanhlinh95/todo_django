from django import forms
from .models import Todo

"""
Todo Form Create
"""
class TodoFormCreate(forms.ModelForm):
    title = forms.CharField(min_length=6, max_length=100, required=True, error_messages={
        'required': 'bat buoc nhap',
        'max_length': 'Your name is too long.',
        'min_length': 'Your name is min lenght 6.',
    })
    description = forms.CharField(min_length=6, max_length=100, required=True, error_messages={
        'required': 'bat buoc nhap.',
        'max_length': 'Your name is too long.',
        'min_length': 'Your name is min lenght 6.',
    })

    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']


    def save(self, commit=True):
        todo = super().save(commit=False)
        if commit:
            todo.save()
        return todo




"""
Todo Form Update
"""
class TodoFormEdit(forms.ModelForm):
    title = forms.CharField(min_length=6, max_length=100, required=True, error_messages={
        'required': 'bat buoc nhap',
        'max_length': 'Your name is too long.',
        'min_length': 'Your name is min lenght 6.',
    })
    description = forms.CharField(min_length=6, max_length=100, required=True, error_messages={
        'required': 'bat buoc nhap.',
        'max_length': 'Your name is too long.',
        'min_length': 'Your name is min lenght 6.',
    })

    class Meta:
        model = Todo
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)