from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view

from .models import AbstUser, Publication
from .serializers import AbstUserSerializer, PublicationSerializer


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


class PublicationByTitelView(APIView):
    def get(self, request, titel, format=None):
        publication = Publication.objects.get(titel = titel)
        serializer = PublicationSerializer(publication)
        return Response(serializer.data)

    def put(self, request, titel, format=None):
        publication = Publication.objects.get(titel = titel)
        serializer = PublicationSerializer(publication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, titel, format=None):
        publication = Publication.objects.get(titel = titel)
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(('GET',))        
def add_upvoted(request, titel):
    if request.method == 'GET':
        publication = Publication.objects.get(titel = titel)
        publication.upvoted += 1
        publication.save()
        serializer = PublicationSerializer(publication)    
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(('GET',))        
def add_downvoted(request, titel):
    if request.method == 'GET':
        publication = Publication.objects.get(titel = titel)
        publication.downvoted += 1
        publication.save()
        serializer = PublicationSerializer(publication)    
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

#class PublicationByAutorView(APIView):
#    def get(self, request, user, format=None):
#        publication = Publication.objects.get(autor = request.user)
#        serializer = PublicationSerializer(publication)
#        return Response(serializer.data)
#
#    def put(self, request, titel, user, format=None):
#        publication = Publication.objects.get(autor = user)
#        serializer = PublicationSerializer(publication)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, titel, user, format=None):
#        publication = Publication.objects.get(autor = user)
#        publication.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)