from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Items,Movies

class Register(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    def save(self,commit=True):
        user=super(Register,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
            return user

class additems(forms.ModelForm):
    class Meta:
        model=Items
        fields=["name","designation","img"]

class Movie_form(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'year', 'description', 'img']