from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=300)
    date_of_birth = models.DateTimeField(null=False, default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return "Student name is "+self.name