from rest_framework2 import serializers

from tests.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
