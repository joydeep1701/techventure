from django import forms
from .models import CalenderEvent

class CalenderEventForm(forms.ModelForm):
    class Meta:
        model = CalenderEvent
        fields = ['creator_name','event_level','event_name','location','start_date','start_time','description']
        widgets = {
            'creator_name': forms.HiddenInput(
                attrs={'id': 'creator_name', 'required': True, 'placeholder': 'Your Name'}
            ),
            'start_date':forms.HiddenInput(
                attrs={'id': 'start_date', 'required': True, 'placeholder': 'Start Date'},
            ),
            'description':forms.Textarea(
                attrs={'rows':3}
            ),
        }
