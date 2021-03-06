from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from home.models import Product,Profile,Review,Rate_Choices

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','photo','details','category','price','author','publication','ISBN']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['contact_no','profession','interest','profile_image','user_type','rating','pradesh','district','palika','ward_no','local_add']


class RateForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rate','text']