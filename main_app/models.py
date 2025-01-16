from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

APPLICATION_STATUSES = (
    ("TS", "To Submit"),
    ("SU", "Submitted"),
    ("R", "Rejected"),
    ("P", "Progressing to Next Stage"),
    ("SC", "Successful"),
)

TITLES = (
    ("MR", "Mr"),
    ("MISS", "Miss"),
    ("MRS", "Mrs"),
    ("MX", "Mx"),
    ("MS", "Ms"),
    ("O", "Other"),
)

EDUCATION_TYPES = (
    ("B", "Bachelor"),
    ("M", "Masters"),
    ("PHD", "Philosophical Doctorate"),
    ("D", "Diploma"),
    ("MD", "Medical Doctorate"),
    ("O", "Other"),
)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField()
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, choices=APPLICATION_STATUSES, default=APPLICATION_STATUSES[0][0]
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
        return f"A {self.type} progress item for {self.application.position} at {self.application.company_name}."

    def get_absolute_url(self):
        return reverse(
            "application-detail", kwargs={"application_id": self.application.id}
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=4, choices=TITLES, default=TITLES[0][0], blank=True, null=True
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    headline = models.CharField(max_length=250, blank=True, null=True)
    profile_picture_url = models.CharField(max_length=250, blank=True, null=True)
    resume_url = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.get_title_display()} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={"pk": self.id})


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return f"A skill named {self.skill} for {self.profile}'s profile."


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_current = models.BooleanField()
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"An experience entry as {self.position} at {self.company_name} for {self.profile}'s profile."


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    is_current = models.BooleanField()
    institution_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    type = models.CharField(
        max_length=3, choices=EDUCATION_TYPES, default=EDUCATION_TYPES[0][0]
    )

    def __str__(self):
        return f"An educational record for a {self.type} of {self.qualification} at {self.institution_name} for {self.profile}'s profile."


# TODO - Create models for Applicants and Ad's
