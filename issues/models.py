from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Team

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Issue(models.Model):
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=512)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True, related_name='assignee'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True
    )
    assigned_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("URL_NAME", args=[self.id])