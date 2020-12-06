from .models import AbstUser
from rest_framework import serializers


class AbstUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstUser
        fields = ['username', 'last_name', 'first_name', 'email', 'about_yourself']
