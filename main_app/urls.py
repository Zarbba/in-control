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
        "progressitems/<int:pk>/delete/",
        views.ProgressItemDelete.as_view(),
        name="progress-item-delete",
    ),
    path("accounts/signup/", views.signup, name="signup"),
]
