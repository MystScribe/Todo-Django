from django import forms

class UserSignUpForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 12px; outline: 0;  '
    }))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 49px; outline: 0;  '
    }))
    FirstName = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'FirstName',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 17px; outline: 0;  '
    }))
    LastName = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'LastName',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 14px; outline: 0;  '
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 17px; outline: 0;  '
    }))


class UserSignInForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 12px; outline: 0;  '
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'style': 'width: 80%; padding: 15px; border: solid 1px black; border-radius: 10px; background-color: transparent; margin-left: 17px; outline: 0;  '
    }))
