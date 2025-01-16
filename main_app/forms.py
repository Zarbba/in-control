from django import forms
from .models import ProgressItem


class ProgressItemForm(forms.ModelForm):
    class Meta:
        model = ProgressItem
        fields = ["action_date", "type", "notes"]
        widgets = {
            "action_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
        }
