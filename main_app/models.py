from django.db import models
from django.urls import reverse


# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('habit-detail', kwargs={'habit_id': self.id})