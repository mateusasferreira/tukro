from django.shortcuts import render
from rest_framework import (
    viewsets, permissions, response, status
)
from communities.models import Community
from communities.permissions import CommunityPermission
from communities.serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, CommunityPermission)
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def create(self, request):
        serializer = CommunitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)

            return response.Response(serializer.data, status.HTTP_201_CREATED)

        return response.Response({'errors': serializer.data}, status=status.HTTP_400_BAD_REQUEST)