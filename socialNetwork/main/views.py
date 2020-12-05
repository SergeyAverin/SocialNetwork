from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from .models import AbstUser
from .serializers import AbstUserSerializer


class UserByUserNameView(APIView):
    def get(self, request, username, format=None):
        user = AbstUser.objects.get(username= username)
        serializer = AbstUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        user = AbstUser.objects.get(username= username)
        serializer = AbstUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        user = AbstUser.objects.get(username= username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)