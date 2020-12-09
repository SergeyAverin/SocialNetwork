from .models import AbstUser, Publication
from rest_framework import serializers


class AbstUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstUser
        fields = ['username', 'last_name', 'first_name', 'email', 'about_yourself']


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__' 