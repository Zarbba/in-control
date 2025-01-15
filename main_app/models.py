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
    created_date = models.DateField()
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, choices=APPLICATION_STATUS, default=APPLICATION_STATUS[0][0]
    )

    def get_absolute_url(self):
        return reverse("application-detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"An application for {self.position} at {self.company_name} made on {self.created_date}"


class ProgressItem(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    action_date = models.DateField()
    notes = models.CharField(max_length=250)

    def __str__(self):
        return f"A {self.type} progress item."  # TODO - Figure out how to call the application here to add it to the string.
