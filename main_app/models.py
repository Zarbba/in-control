from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

APPLICATION_STATUS = (
    ("TS", "To Submit"),
    ("SU", "Submitted"),
    ("R", "Rejected"),
    ("P", "Progressing to Next Stage"),
    ("SC", "Successful"),
)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_applied = models.DateField()
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, choices=APPLICATION_STATUS, default=APPLICATION_STATUS[0][0]
    )

    def get_absolute_url(self):
        return reverse("application-detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"An application for {self.position} at {self.company_name} made on {self.date_applied}"
