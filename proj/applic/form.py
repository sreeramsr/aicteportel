from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import DocumentUpload

from .models import Institution

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        exclude = ['user'] 

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields='__all__'
        exclude = ['user']  # Exclude user field from the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'accept': 'application/pdf'})

class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
  class Meta:
    model=User
    fields=['username','email','password1','password2']