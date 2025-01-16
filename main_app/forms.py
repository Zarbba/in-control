from django import forms
from .models import ProgressItem, Experience, Education, Skill


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


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "start_date",
            "end_date",
            "is_current",
            "company_name",
            "position",
            "description",
        ]
        widgets = {
            "start_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
            "end_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            "start_date",
            "end_date",
            "is_current",
            "institution_name",
            "qualification",
            "type",
        ]
        widgets = {
            "start_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
            "end_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["skill"]
