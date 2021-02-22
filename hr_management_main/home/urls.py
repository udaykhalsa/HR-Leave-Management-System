from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('applications/', views.applications_view, name='applications'),
]