from django import forms
from .models import dream

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
