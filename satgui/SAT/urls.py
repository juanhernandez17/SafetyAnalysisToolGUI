from django.urls import path
from . import views

urlpatterns = [
    path('SAT/', views.Sat.as_view(), name='SAT'),
]
