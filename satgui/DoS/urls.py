from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('DoS/', views.DoS.as_view(), name='DoS'),
    path('file/', views.File.as_view(), name='fileform'),
    path('file/<int:id>', views.File.as_view(), name='getfile'),

]
