from django.urls import path, include
from rest_framework.routers import SimpleRouter
from users.views import RegistrationView


urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
]

