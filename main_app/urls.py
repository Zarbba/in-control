from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path(
        "applications/create/",
        views.ApplicationCreate.as_view(),
        name="application-create",
    ),
    path("applications/", views.ApplicationList.as_view(), name="application-index"),
    path(
        "applications/<int:application_id>/",
        views.application_detail,
        name="application-detail",
    ),
    path(
        "applications/<int:application_id>/add-progress-item",
        views.add_progress_item,
        name="add-progress-item",
    ),
    path(
        "applications/<int:pk>/update",
        views.ApplicationUpdate.as_view(),
        name="application-update",
    ),
    path(
        "applications/<int:pk>/delete/",
        views.ApplicationDelete.as_view(),
        name="application-delete",
    ),
    path(
        "progressitems/<int:pk>/update",
        views.ProgressItemUpdate.as_view(),
        name="progress-item-update",
    ),
    path(
        "profiles/<int:pk>/update",
        views.ProfileUpdate.as_view(),
        name="profile-update",
    ),
    path(
        "educations/<int:pk>/delete/",
        views.EducationDelete.as_view(),
        name="education-delete",
    ),
    path(
        "experience/<int:pk>/delete/",
        views.ExperienceDelete.as_view(),
        name="experience-delete",
    ),
    path(
        "skills/<int:pk>/delete/",
        views.SkillDelete.as_view(),
        name="skill-delete",
    ),
    path(
        "progressitems/<int:pk>/delete/",
        views.ProgressItemDelete.as_view(),
        name="progress-item-delete",
    ),
    path("accounts/signup/", views.signup, name="signup"),
    path("profiles/<int:profile_id>/", views.profile_detail, name="profile-detail"),
    path(
        "profiles/<int:profile_id>/add-skill",
        views.add_skill,
        name="add-skill",
    ),
    path(
        "profiles/<int:profile_id>/add-experience",
        views.add_experience,
        name="add-experience",
    ),
    path(
        "profiles/<int:profile_id>/add-education",
        views.add_education,
        name="add-education",
    ),
]
