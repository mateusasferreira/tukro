from django.shortcuts import render
from rest_framework import views, response, status

from users.serializers import RegistrationSerializer

class RegistrationView(views.APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
