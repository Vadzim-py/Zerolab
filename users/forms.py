from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, SetPasswordForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-3', 'placeholder': 'Confirm your password'}))
    is_superuser = forms.BooleanField(required=False, label='Is superuser')
    is_staff = forms.BooleanField(required=False, label='Is staff')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_superuser', 'is_staff')


class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-3'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-3'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-3'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-3'}))
    is_superuser = forms.BooleanField(required=False, label='Is superuser')
    is_staff = forms.BooleanField(required=False, label='Is staff')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_superuser', 'is_staff')


class UserSetPassForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=24,
        label='New password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control py-3',
            'placeholder': 'Enter a new password'
        })
    )
    new_password2 = forms.CharField(
        max_length=24,
        label='Confirm new password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control py-3',
            'placeholder': 'Repeat a new password'
        })
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')
