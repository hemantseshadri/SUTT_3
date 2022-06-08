from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category,inventory


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class Additemform(forms.ModelForm):
    class Meta:
        model = inventory
        fields = ('Item_name','Quantity','category')


    #Item_name = forms.CharField()
    #Quantity = forms.IntegerField()
    #category = forms.ModelChoiceField(queryset=Category.objects.all())

class Addcategoryform(forms.Form):
    category = forms.CharField()

class Additemform_two(forms.Form):
    Item_name = forms.CharField()
    Quantity = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
