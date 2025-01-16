from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application
from .forms import ProgressItemForm
from django import forms


class Home(LoginView):
    template_name = "home.html"


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ["created_date", "company_name", "position", "status"]

    def get_form(self, form_class=None):
        form = super(ApplicationCreate, self).get_form(self.get_form_class())

        form.fields["created_date"].widget = forms.DateInput(
            format=("%Y-%m-%d"), attrs={"placeholder": "Select a date", "type": "date"}
        )
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ["created_date", "company_name", "position", "status"]

    def get_form(self, form_class=None):
        form = super(ApplicationUpdate, self).get_form(self.get_form_class())

        form.fields["created_date"].widget = forms.DateInput(
            format=("%Y-%m-%d"), attrs={"placeholder": "Select a date", "type": "date"}
        )
        return form


class ApplicationList(LoginRequiredMixin, ListView):
    model = Application

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = "/applications/"


# TODO - Create a profile DetailView(custom) and EditView
# TODO - Create Ad ListView, DetailView, CreateView, EditView and DeleteView


@login_required
def application_detail(request, application_id):
    application = Application.objects.get(id=application_id)
    progress_item_form = ProgressItemForm()
    return render(
        request,
        "applications/detail.html",
        {"application": application, "progress_item_form": progress_item_form},
    )


def add_progress_item(request, application_id):
    form = ProgressItemForm(request.POST)
    if form.is_valid():
        new_progress_item = form.save(commit=False)
        new_progress_item.application_id = application_id
        new_progress_item.save()
    return redirect("application-detail", application_id=application_id)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("application-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
