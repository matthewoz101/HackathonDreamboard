from django import forms
from .models import dream

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DreamForm(forms.ModelForm):
    class Meta:
        model = dream
        fields = '__all__'

        labels = {
            'first_name' : 'First name',
            'last_name' : 'Last name',
            'dreamItem' : 'Dream',
        }


        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dreamItem': forms.Textarea(attrs={'class': 'form-control'}),
        }



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
