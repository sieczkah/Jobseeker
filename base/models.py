from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class JobApplication(models.Model):
    APPLIED = "AP"
    CONTACTED = "CO"
    INTERVIEWED = "IV"
    INTERVIEWED = "IV"
    EVALUATED = "EV"
    JOB_PROPOSISTION = "JP"
    DENIED = "DE"
    ACCEPPTED = "AC"
    REJECTED = "RE"
    APPLICATION_STATUS_CHOICES = [
        (APPLIED, "APPLIED"),
        (CONTACTED, "CONTACTED"),
        (INTERVIEWED, "INTERVIEWED"),
        (EVALUATED, "EVALUATED"),
        (JOB_PROPOSISTION, "JOB_PROPOSISTION"),
        (DENIED, "DENIED"),
        (ACCEPPTED, "ACCEPPTED"),
        (REJECTED, "REJECTED"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    posistion = models.CharField(max_length=250, null=True, blank=True)
    company = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        choices=APPLICATION_STATUS_CHOICES, default=APPLIED, max_length=2
    )
    apply_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    link = models.CharField(max_length=1000, null=False, blank=False)
    salary = models.CharField(
        max_length=100, null=True, blank=True, default="Not specified"
    )

    def __str__(self):
        return f"{self.posistion} - {self.company} - {self.status} updated: {self.update_date}"


# class AiJobData(models.Model):
#     id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
#     key_skills = models.TextField()
#     questions = models.TextField()
#     study_resources = models.TextField()
