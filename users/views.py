from django.http import Http404
from django.shortcuts import render
from rest_framework import views, response, status, permissions

from users.serializers import UserSerializer
from users.models import User

class RegistrationView(views.APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class UsersList(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return response.Response(serializer.data)

class UsersDetail(views.APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)

            return response.Response(serializer.data)
        except User.DoesNotExist:
            raise Http404