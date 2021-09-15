from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegisterForm,  UserLoginForm, UserUpdateForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User as Userdb




# Create your views here.


class Login(TemplateView):
	template_name = 'login/login.html'
	form = UserLoginForm

	def get(self, request):
		form = self.form()
		if request.user.is_authenticated:
		 	return redirect('home')
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form(request.POST)
		next = request.GET.get('next')
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			login(request, user)
			if next:
				return redirect(next)
			return redirect('home')  # Not working
		return render(request, self.template_name, {'form': form})


class Register(View):
	template_name = 'login/register.html'
	form = UserRegisterForm

	def get(self, request):
		form = self.form()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('login')
		return render(request, self.template_name, {'form': form})


class User(TemplateView):
	template_name = 'login/user.html'
	def get(self, request):
		if request.user.is_authenticated:
		 	return redirect('home')
		return render(request, self.template_name)

class Logout(TemplateView):
	def get(self, request):
		logout(request)
		return redirect('/')


class Account(TemplateView):
	template_name = 'login/account.html'
	pform = PasswordChangeForm
	uform = UserUpdateForm
	def get(self, request):
		usr = Userdb.objects.get(id=request.user.id)
		pform = self.pform(request.user)
		return render(request, self.template_name, {'pform': pform,'usr':usr})

	def post(self, request):
		usr = Userdb.objects.get(id=request.user.id)
		pform = self.pform(request.user, request.POST)
		if pform.is_valid():
				user = pform.save()
				update_session_auth_hash(request, user)  # Important!
				messages.success(
					request, 'Your password was successfully updated!')
				return redirect('login')
		return render(request, self.template_name, {'pform': pform, 'usr': usr})
