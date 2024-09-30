from django.urls import path
from .views import task_list, accept_task, complete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('accept/<int:task_id>/', accept_task, name='accept_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
]
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Другие ваши URL
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
