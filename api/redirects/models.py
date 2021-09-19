from django.db import models


class Redirect(models.Model):
    key = models.CharField(max_length=255, default="", unique=True)
    url = models.URLField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

