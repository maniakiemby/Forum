from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm, UserModel
from django.views.generic import (
    FormView,
    UpdateView,
)

from .forms import (
    CreateUserForm,
    UpdateUserForm,
)


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


class UserView(LoginRequiredMixin, UpdateView):
    login_url = "user/accounts/login/"
    template_name = 'user_panel/user_view.html'
    form_class = UpdateUserForm
    success_url = '.'

    def get_object(self):
        id_ = self.request.user.id
        # username = self.kwargs.get('username')
        return get_object_or_404(User, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)
