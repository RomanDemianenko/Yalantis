from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()
    num_lectures = models.PositiveIntegerField()