
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# class UserPublicSerializer(serializers.Serializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']

    # user = serializers.CharField(read_only=True)
