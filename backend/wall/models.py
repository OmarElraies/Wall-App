from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()


    def __str__(self):
        """A string representation of the Post."""
        return self.title