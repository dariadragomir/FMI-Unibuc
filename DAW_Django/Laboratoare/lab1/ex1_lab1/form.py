from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser  # Model personalizat

class CustomUserCreationForm(UserCreationForm):
    telefon = forms.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username","email", "telefon", "password1", "password2")
    def save(self, commit=True):
        user = super().save(commit=False)
        user.telefon = self.cleaned_data["telefon"]
        if commit:
            user.save()
        return user

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    ramane_logat = forms.BooleanField(
        required=False,
        initial=False,
        label='Ramaneti logat'
    )

    def clean(self):        
        cleaned_data = super().clean()
        ramane_logat = self.cleaned_data.get('ramane_logat')
        return cleaned_data
