from django import forms
from .models import TYPES


class PersonForm(forms.Form):

    first_name = forms.CharField(label='First name', max_length=32)
    last_name = forms.CharField(label='Last name', max_length=32)
    description = forms.CharField(label='Description', max_length=512)


class EmailForm(forms.Form):

    email = forms.EmailField(label='Enter your email')
    type = forms.ChoiceField(label='Choose email type', choices=TYPES)


class SearchForm(forms.Form):

    phrase = forms.CharField(label='Enter search phrase', max_length=128)


