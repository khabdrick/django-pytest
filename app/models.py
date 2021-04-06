from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

