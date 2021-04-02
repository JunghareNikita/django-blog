from django.db import models
from django.contrib.auth.models import User

class BlogsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.user.username