import random
import string
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


from userprofile.forms import NewAccountForm
punctuation = '!$%?#@'

class CreateNewAccount(LoginRequiredMixin, CreateView): #login ca sa putem sa vedem dupa autentificare, si create pentru ca vreau sa creez utilizator
    model = User
    template_name = 'aplicatie1/visualizations_form.html'
    form_class = NewAccountForm#capurile pe care vrem sa le vedem in formular, facem un form class, putem sa rescriem proprietati din formular si sa punem conditii de validare

    def form_valid(self, form):
        if form.is_valid() and form.errors is False:
            form.save(commit=False)
        return super(CreateNewAccount, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateNewAccount, self).form_invalid(form)

    #ajugem dupa ce a fost salvata cu succes inregistrarea in baza de date, generam parola dupa ce s-a salvat utlizatorul
    #spunem structura parolei - 8 caractere, sa aiba litere mari/mici, cifre si semn se punctuatie
    def get_success_url(self):

        psw = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation)
            for _ in range(8))
        if User.objects.filter(id=self.object.id).exists():
            user_instance = User.objects.get(id=self.object.id) #variabila in care salvez obiectul
            user_instance.set_password(psw)
            user_instance.save() #salvez noul utilzator cu noua parola
            content = f"Authentification dates are: \n username: {user_instance.username} \n password: {psw}"
            msg_html = render_to_string('registration/invite_user.html', {"content_email": content})
            email = EmailMultiAlternatives(subject="Invite user", body=content, from_email='contact@test.ro',
                                           to=[user_instance.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('visualizations:lista_vizualizare')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'userprofile/password-change.html'
    success_url = reverse_lazy('userprofile:password-change-done-view')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'userprofile/password-reset-done.html'
