from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		Model = CustomUser
		fields = ['email']

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		Model = CustomUser
		fields = ['email']
