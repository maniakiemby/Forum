from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (
    RegistrationView,
    UserView
)

app_name = 'user_panel'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', RegistrationView.as_view(), name='create-user'),
    path('panel/', UserView.as_view(), name='user-view'),

    path('password/', auth_views.PasswordChangeView.as_view(template_name='user_panel/password_change.html', success_url='../password-change/'), name='password'),
    path('password-change/', auth_views.PasswordChangeDoneView.as_view(template_name='user_panel/password_change_done.html'), name='password_change_done'),

    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(success_url='done/'), name='password_reset'),
    path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url='../../done/'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
