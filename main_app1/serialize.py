from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'id',
            'first_name',
            'last_name'
        )


class UserVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['token']