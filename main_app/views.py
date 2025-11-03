from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from .models import Habit, Completion
from .forms import HabitForm
# from .forms import CompletionForm


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
    form_class = HabitForm 
    template_name = 'main_app/habit_form.html'
    def get_success_url(self):
        # after saving, redirect to the habit detail page for this habit
        return reverse('habit-detail', kwargs={'habit_id': self.object.id})
    # success_url = reverse_lazy('habit-index')
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)



class UpdateHabit(UpdateView):
    model = Habit
    form_class = HabitForm    
    template_name = 'main_app/habit_form.html'
    def get_success_url(self):
        # after saving, redirect to the habit detail page for this habit
        return reverse('habit-detail', kwargs={'habit_id': self.object.id})
    # fields = ['description']

class DeleteHabit(DeleteView):
    model = Habit
    success_url='/habitrabbits/'

class Home(LoginView):
    template_name = 'home.html'

@login_required
def habit_index(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/index.html', {'habits': habits})

@login_required
def habit_detail(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    return render(request, 'habits/detail.html', {'habit': habit})

@login_required
def mark_complete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    today = timezone.now().date()
    already_done = habit.completions.filter(timestamp__date=today).exists()
    if not already_done:
        Completion.objects.create(habit=habit)
    return redirect('habit-detail', habit_id=habit.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('habit-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def login(request):
    error_message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('habit-index')  # redirect wherever you want
        else:
            error_message = 'Invalid username or password'
    else:
        form = AuthenticationForm()
    
    context = {'form': form, 'error_message': error_message}
    return render(request, 'login.html', context)