from venv import create
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)


