from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Adds email field to Django Form
    
    class Meta:
        model = User #will create new user
        fields = ['username','email','password1','password2']
		
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("User Does Not Exist")
			if not user.check_password(password):
				raise forms.ValidationError("Wrong Password")
			if not user.is_active:
				raise forms.ValidationError("User is not active")
		return super(UserLoginForm, self).clean(*args,**kwargs)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
