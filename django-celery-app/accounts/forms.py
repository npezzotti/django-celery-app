from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .tasks import send_welcome_email_task

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ("username","email", "password1", "password2")
        help_texts = {
            "username":None,
        }

    def send_email(self):
        send_welcome_email_task.delay(self.cleaned_data["username"], self.cleaned_data["email"])

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
