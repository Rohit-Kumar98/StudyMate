from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Resource, Comment

class SignupForm(forms.ModelForm):
    registration_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    

class LoginForm(forms.Form):
    registration_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class ResourceUploadForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            'title',
            'subject',
            'resource_type',
            'semester',
            'description',
            'file'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']