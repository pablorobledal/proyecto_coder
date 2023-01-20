from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EditarPerfil(forms.Form):
    
    username=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=100)
    bio=forms.TextInput()
    avatar=forms.ImageField()



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

