#adaugam prima clasa de form
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class NewAccountForm(forms.ModelForm):

    class Meta: #ne ajuta sa numim anumite proprietati cum ar fi lista de fileduri pe care o folosim
        model = User
        fields = ['first_name', 'last_name', 'email', 'username'] #aceste fields deja sunt in baza noastra de date, parola va fi generata automat
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'first name', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        #validare ex sa nu introducem adresa de mail duplicata:

    def clean(self):
        field_data = self.cleaned_data
        email_value = field_data.get('email') #din dictionarul filed_data accesez cheia email
        username_value = field_data.get('username')
        #verificam daca e-mail ul/username-ul mai exista in baza de date:
        if User.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(['Email already exists, please introduce an unique email'])
        if User.objects.filter(username=username_value).exists():
            self._errors['username'] = self.error_class(['Username already exists, please introduce an unique username!'])
        return field_data


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())