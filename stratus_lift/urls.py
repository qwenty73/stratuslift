from django.contrib import admin
from django.urls import path
from tasks.views import task_list, accept_task, complete_task, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('accept/<int:task_id>/', accept_task, name='accept_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
