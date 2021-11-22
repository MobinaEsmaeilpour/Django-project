from django import forms
from django.contrib.auth.forms import RegisterPage
from django.forms import fields
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class NewUserForm(FormView):
    email = forms.EmailField(required= True)


    class Meta :
        model = FormView
        fields = ("username" , "email" "password1" , "password2")


    def save(self, commit=True):
        user = super(FormView, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user        