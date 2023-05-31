# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('validate_policy/', views.validate_policy, name='validate_policy'),
]