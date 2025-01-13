from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Application
from django import forms


class ApplicationCreate(CreateView):
    model = Application
    fields = ["date_applied", "company_name", "position", "status"]

    def get_form(self, form_class=None):
        form = super(ApplicationCreate, self).get_form(self.get_form_class())

        form.fields["date_applied"].widget = forms.DateInput(
            format=("%Y-%m-%d"), attrs={"placeholder": "Select a date", "type": "date"}
        )
        return form


class ApplicationUpdate(UpdateView):
    model = Application
    fields = ["date_applied", "company_name", "position", "status"]

    def get_form(self, form_class=None):
        form = super(ApplicationUpdate, self).get_form(self.get_form_class())

        form.fields["date_applied"].widget = forms.DateInput(
            format=("%Y-%m-%d"), attrs={"placeholder": "Select a date", "type": "date"}
        )
        return form


class ApplicationList(ListView):
    model = Application


class ApplicationDetail(DetailView):
    model = Application
