
from  django import forms
from .models import Collagedetail,Collagelist
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db import models


class student_form(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder': ' enter name '})
                           ,required= True, max_length = 100)
    url    = forms.CharField(widget=  forms.URLInput(attrs ={'class':'form-control','placeholder': 'enter url'})
                           ,required= True, max_length = 100)
 
    emailid = forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control','placeholder': 'enter email'})
                           ,required= True, max_length = 150)
 
    about = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','placeholder': 'about it'})
                           ,required= False, max_length= 100)
    
    class Meta():
        model = Collagelist
        fields = ['name', 'emailid', 'url', 'about']
"""

class student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput() , required=True, max_length=100)
    url = forms.URLField(widget=forms.URLInput(), required=True, max_length=100)

    emailid = forms.EmailField(widget=forms.EmailInput(), required=True, max_length=150)

    about = forms.TextField(widget=forms.Textarea(), required=False, max_length=100)

    class Meta():
        model = Collagelist
        fields = ['name', 'emailid', 'url', 'about']

"""

class  userform(forms.ModelForm):
    username = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control', 'placeholder' : 'Enter username'}),
                               required= True, max_length= 50)

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
        , required=True, max_length=50)

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
        , required=True, max_length=50)

    email = forms.CharField(  widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
        , required=True, max_length=50)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
                               , required=True, max_length=50)

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'})
                               , required=True, max_length=50)

    class Meta():
        model = User
        fields = ['username','email','first_name','last_name','password','confirm_password']

        def clean_username(self):
            user = self.cleaned_data['username']
            try:
                match = User.objects.get(username =user)

            except:
                return self.cleaned_data['username']
            raise forms.ValidationError("Username already exist")

        def clean_email(self):
            email = self.cleaned_data['email']
            try:
                mt = validate_email(email)

            except:
                return forms.ValidationError("email is not in correct format")

            return email


        def clean_confirm_password(self):
            pas = self.cleaned_data['password']
            cpas = self.cleaned_data['confirm_password']
            MIN_LENGTH =8
            if pas  and cpas:
                if pas != cpas:
                    raise forms.ValidationError("password and confirmed password does not matched")
                else:
                    if len(pas) < MIN_LENGTH:
                        raise forms.ValidationError("password should have at least %d character" %MIN_LENGTH)

                    if pas.isdigit():
                        raise forms.ValidationError("password should not all numeric")

