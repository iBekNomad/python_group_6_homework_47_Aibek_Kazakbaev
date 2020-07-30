from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class MemoForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    text = forms.CharField(max_length=3000, required=True, label='Detailed description', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status', initial=default_status)
    execution_date = forms.DateField(required=True, label='Execution date', input_formats=['%Y-%m-%d'],
                                     widget=forms.DateInput(attrs={'type': 'date'}))
