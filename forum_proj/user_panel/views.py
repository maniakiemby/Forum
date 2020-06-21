from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    FormView,
    
)

from .forms import CreateUserForm


class CreateUserView(FormView):
    template_name = 'registration/registration.html'
    form_class = CreateUserForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(CreateUserView, self).form_valid(form)
