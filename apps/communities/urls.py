from django.urls import include, path
from rest_framework import routers

from  apps.communities.views import CommunityViewSet

router = routers.SimpleRouter()
router.register(r'communities', viewset=CommunityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]