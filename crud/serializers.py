from rest_framework import  serializers
from django.contrib.auth.models import User
# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined']