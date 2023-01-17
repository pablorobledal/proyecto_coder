from django import forms

class EditarPerfil(forms.Form):
    
    username=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=100)
    bio=forms.TextInput()
    avatar=forms.ImageField()