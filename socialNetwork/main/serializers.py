from .models import AbstUser
from rest_framework import serializers


class AbstUserSerializer(serializers.ModelSerializer):
    #username = serializers.CharField()
    #lastName = serializers.CharField()
    #firstName = serializers.CharField()
    #email = serializers.EmailField()
    #about_yourself = serializers.CharField()
    #gender = serializers.c


    class Meta:
        model = AbstUser
        fields = ['username', 'last_name', 'first_name', 'email', 'about_yourself']