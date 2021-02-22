from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('applications/', views.applications_view, name='applications'),
    path('apply_leave/', views.apply_leave_view, name='apply_leave'),
    path('leave_status/', views.leave_status_view, name='leave_status'),
]