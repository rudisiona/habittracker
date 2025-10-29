from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Habit



# Create your views here.

# class Habit:
#      def __init__(self, name, description):
#         self.name = name
#         self.description = description

# habits = [
#     Habit('drink water', '3 times a day'),
#     Habit('take vitamins', 'once a day')
# ]

class CreateHabit(CreateView):
    model = Habit
    fields ='__all__'

class UpdateHabit(UpdateView):
    model = Habit
    fields = ['description']

class DeleteHabit(DeleteView):
    model = Habit
    success_url='/habitrabbits/'

def home(request):
    return render(request, 'home.html')

def habit_index(request):
    habits = Habit.objects.all()
    return render(request, 'habits/index.html', {'habits': habits})

def habit_detail(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    return render(request, 'habits/detail.html', {'habit': habit})