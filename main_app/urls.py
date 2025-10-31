from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habitrabbits/', views.habit_index, name='habit-index'),
    path('habitrabbits/<int:habit_id>/', views.habit_detail, name='habit-detail'),
    path('habitrabbits/create/', views.CreateHabit.as_view(), name='create-habit'),
    path('habitrabbits/<int:pk>/update/', views.UpdateHabit.as_view(), name='update-habit'),
    path('habitrabbits/<int:pk>/delete/', views.DeleteHabit.as_view(), name='delete-habit'),
    path('habitrabbits/<int:habit_id>/complete/', views.mark_complete, name='mark-complete')

]