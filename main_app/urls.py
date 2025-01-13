from django.urls import path
from . import views

urlpatterns = [
    path(
        "applications/create/",
        views.ApplicationCreate.as_view(),
        name="application-create",
    ),
    path(
        "applications/<int:pk>/update",
        views.ApplicationUpdate.as_view(),
        name="application-update",
    ),
    path(
        "applications/<int:pk>/",
        views.ApplicationDetail.as_view(),
        name="application-detail",
    ),
    path(
        "applications/<int:pk>/delete/",
        views.ApplicationDelete.as_view(),
        name="application-delete",
    ),
    path("applications/", views.ApplicationList.as_view(), name="application-index"),
]
