from django.urls import path, include
from users.views import RegistrationView, UsersList, UsersDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', UsersList.as_view(), name="users"),
    path('<int:id>/', UsersDetail.as_view(), name="user"),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
]

