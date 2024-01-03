from django import forms
from . models import Movies

class Movie_form(forms.ModelForm):
    class Meta:
        model=Movies
        fields= ['name','year','desc','image']