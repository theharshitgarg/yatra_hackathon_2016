from django import forms
from .models import *


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    # email = forms.EmailField(label='Email')
    # message = forms.Textarea(label='Message122')
