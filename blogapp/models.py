from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# class Post inheritance models from Model


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # magic method
    def __str__(self):
        return self.title
