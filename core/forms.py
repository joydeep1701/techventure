from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Enter Your First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Enter Your Last Name')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2',)

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')
