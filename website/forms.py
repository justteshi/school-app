from django.contrib.auth import get_user_model
from django import forms
#check for unique username and email
not_allowed_usernames = ['abc', '123']
User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'id':'user-password'
            }
        )
    )
    password2 = forms.CharField(
        label='Cinfirm Password',
        widget=forms.PasswordInput(
            attrs={
                'id':'user-confirm-password'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if username in not_allowed_usernames:
            raise forms.ValidationError('This is invalid username, please pick another.')

        if qs.exists():
            raise forms.ValidationError('This is invalid username, please pick another.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError('This email has been used.')
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id':'user-password'
            }
        )
    )
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('This is invalid user.')
        return username
