from django.urls import path
from . import views

urlpatterns = [
    path("applications/", views.ApplicationList.as_view(), name="application-index")
]
