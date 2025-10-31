from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


# Create your models here.

WEEK_DAYS = [
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
    ('sun', 'Sunday'),
]


class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    days = ArrayField(models.CharField(max_length=3, choices=WEEK_DAYS), blank=True, default=list)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('habit-detail', kwargs={'habit_id': self.id})
    
    def get_day_labels(self):
        label_map = dict(WEEK_DAYS)
        return [(day, label_map.get(day, day)) for day in self.days]

class Completion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='completions')
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.habit.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"