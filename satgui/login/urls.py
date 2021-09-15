from django.urls import path 
from . import views

urlpatterns = [
    path('user/', views.User.as_view(), name='user'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
	path('logout/', views.Logout.as_view(), name='logout'),
   	path('account/', views.Account.as_view(), name='account'),

]
