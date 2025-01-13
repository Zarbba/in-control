from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Application


class ApplicationCreate(CreateView):
    model = Application
    fields = ["date_applied", "company_name", "position", "status"]


class ApplicationList(ListView):
    model = Application


class ApplicationDetail(DetailView):
    model = Application
