from rest_framework import serializers

from .models import AbstUser, Publication, Comment


class AbstUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstUser
        fields = ['username', 'last_name', 'first_name', 'email', 'about_yourself']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__' 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 