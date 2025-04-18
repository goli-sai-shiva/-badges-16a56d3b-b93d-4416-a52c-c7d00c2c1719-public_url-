from django.urls import path
from . import views

urlpatterns = [
    path('', views.badge_detail, name='badge_detail'),
]