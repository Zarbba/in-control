from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application, ProgressItem, Profile, Experience, Education, Skill
from .forms import ProgressItemForm, SkillForm, EducationForm, ExperienceForm
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


class ProgressItemUpdate(LoginRequiredMixin, UpdateView):
    model = ProgressItem
    fields = ["type", "action_date", "notes"]

    def get_form(self, form_class=None):
        form = super(ProgressItemUpdate, self).get_form(self.get_form_class())

        form.fields["action_date"].widget = forms.DateInput(
            format=("%Y-%m-%d"), attrs={"placeholder": "Select a date", "type": "date"}
        )
        return form


class ProgressItemDelete(LoginRequiredMixin, DeleteView):
    model = ProgressItem
    success_url = f"/applications/"


class ExperienceDelete(LoginRequiredMixin, DeleteView):
    model = Experience
    success_url = f"/applications/"


class EducationDelete(LoginRequiredMixin, DeleteView):
    model = Education
    success_url = f"/applications/"


class SkillDelete(LoginRequiredMixin, DeleteView):
    model = Skill
    success_url = f"/applications/"


# TODO - Create a profile DetailView(custom) and EditView
# TODO - Create Ad ListView, DetailView, CreateView, EditView and DeleteView


@login_required
def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    skill_form = SkillForm()
    education_form = EducationForm()
    experience_form = ExperienceForm()
    return render(
        request,
        "profiles/detail.html",
        {
            "profile": profile,
            "skill_form": skill_form,
            "education_form": education_form,
            "experience_form": experience_form,
        },
    )


@login_required
def application_detail(request, application_id):
    application = Application.objects.get(id=application_id)
    progress_item_form = ProgressItemForm()
    return render(
        request,
        "applications/detail.html",
        {"application": application, "progress_item_form": progress_item_form},
    )


@login_required
def add_progress_item(request, application_id):
    form = ProgressItemForm(request.POST)
    if form.is_valid():
        new_progress_item = form.save(commit=False)
        new_progress_item.application_id = application_id
        new_progress_item.save()
    return redirect("application-detail", application_id=application_id)


@login_required
def add_skill(request, profile_id):
    form = SkillForm(request.POST)
    if form.is_valid():
        new_skill = form.save(commit=False)
        new_skill.profile_id = profile_id
        new_skill.save()
    return redirect("profile-detail", profile_id=profile_id)


@login_required
def add_education(request, profile_id):
    form = EducationForm(request.POST)
    if form.is_valid():
        new_education = form.save(commit=False)
        new_education.profile_id = profile_id
        new_education.save()
    return redirect("profile-detail", profile_id=profile_id)


@login_required
def add_experience(request, profile_id):
    form = ExperienceForm(request.POST)
    if form.is_valid():
        new_experience = form.save(commit=False)
        new_experience.profile_id = profile_id
        new_experience.save()
    return redirect("profile-detail", profile_id=profile_id)


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
