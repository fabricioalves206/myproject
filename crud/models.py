from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300)
    exam = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    answer = models.TextField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default='', )

    def __str__(self):
        return self.title