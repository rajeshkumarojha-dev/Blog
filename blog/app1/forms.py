from django.forms import ModelForm
from app1.models import Blog
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

class registerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields='__all__'