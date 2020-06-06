from django.urls import path, include


app_name = 'user_panel'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    
]