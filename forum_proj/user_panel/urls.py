from django.urls import path, include

from .views import (
    CreateUserView
)

app_name = 'user_panel'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', CreateUserView.as_view(), name='create-user'),

]