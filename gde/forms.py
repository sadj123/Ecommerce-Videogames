from django.contrib.auth.models import User
from django import forms
from .models import Store, Dispatcher
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required= True)
    first_name= forms.CharField(max_length=30, label= 'Store name')
    class Meta:
        model= User
        fields= ['username', 'email', 'first_name', 'password1', 'password2']
    def save(self, commit= True):
        user= super().save(commit= False)
        user.email= self.cleaned_data['email']
        
        user.first_name= self.cleaned_data['first_name']
        if commit:
            user.save()
        return user
class UserRegistrationFormStore(forms.ModelForm):
    class Meta:
        model= Store
        fields=['street_number', 'street_name', 'city', 'phone', 'photo']
class UserRegistrationForm2(UserCreationForm):
    email= forms.EmailField(required= True)
    first_name= forms.CharField(max_length=30, label= 'First name')
    last_name= forms.CharField(max_length=30, label= 'Last name')
    class Meta:
        model= User
        fields= ['username', 'email', 'first_name','last_name', 'password1', 'password2']
    def save(self, commit= True):
        user= super().save(commit= False)
        user.email= self.cleaned_data['email']
        
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
class UserRegistrationFormDispatcher(forms.ModelForm):
    class Meta:
        model= Dispatcher
        fields=['telephone', 'plate', 'weight', 'height', 'blood_type', 'rh_type', 'photo']
class UserRegistrationForm3(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
class StoreEditForm(forms.ModelForm):
    class Meta:
        model= User
        labels= {
            'first_name': 'Store name'
        }
        fields= ['first_name', 'email']
class StoreEditForm2(forms.ModelForm):
    class Meta:
        model= Store
        fields= ['photo', 'phone', 'city', 'street_name', 'street_number']
class DispatcherEditForm(forms.ModelForm):
    class Meta:
        model = User
        labels={
            'first_name': 'First name',
            'last_name': 'Last name'
        }
        fields= ['email', 'first_name','last_name']
class DispatcherEditForm2(forms.ModelForm):
    class Meta:
        model= Dispatcher
        fields=['telephone', 'plate', 'weight', 'height', 'blood_type', 'rh_type', 'photo']
class AdminEditForm(forms.ModelForm):
    class Meta:
        model = User
        labels={
            'first_name': 'First name',
            'last_name': 'Last name'
        }
        fields= ['email', 'first_name','last_name']
