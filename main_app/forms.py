from django import forms
from .models import Habit, WEEK_DAYS

class HabitForm(forms.ModelForm):
    days = forms.MultipleChoiceField(
        choices=WEEK_DAYS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Days:"
    )

    class Meta:
        model = Habit
        fields = ['name', 'description', 'days']

    def clean_days(self):
        return self.cleaned_data.get('days', [])