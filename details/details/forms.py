from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
#         label="Username or Email*")
#
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'placeholder': 'Password'}))
#
#     captcha = ReCaptchaField(public_key="6Ldp3VciAAAAAHpgmm43io5wmH1LaJdmhF5oSlWV", private_key="6Ldp3VciAAAAAB8AiPKA1pKVOpZRHy_RZSr7sTk6")