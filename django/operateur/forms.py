from django import forms
from .models import User, Operateur

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'operateur']
        widgets = {

            'operateur': forms.RadioSelect(choices=User.drone_choices),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',]

class LoginForm2(forms.ModelForm):
    class Meta:
        model = Operateur
        fields = ['name', 'email', 'numtel','password']



