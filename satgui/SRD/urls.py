from django.urls import path
from . import views

urlpatterns = [
    path('SRD/', views.Srd.as_view(), name='SRD'),

]