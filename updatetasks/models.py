from django.db import models

# Create your models here.
class Task(models.Model):
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField()

    def __str__(self):
        return self.text

    