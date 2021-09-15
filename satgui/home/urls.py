from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('mySystems/', views.Systems.as_view(), name='mySystems'),
    path('', views.Index.as_view(), name='index'),

]
