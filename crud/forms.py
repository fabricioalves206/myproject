from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Question

# Create a user (Model Form)
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class SearchForm(forms.Form):
    exam = forms.CharField(label='Exam', required=False)
    subject = forms.CharField(label='Subject', required=False)

class CreateQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'description', 'exam', 'subject', 'answer']