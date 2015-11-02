from rest_framework2 import serializers

from tests.accounts.models import Account
from tests.users.serializers import UserSerializer


class AccountSerializer(serializers.ModelSerializer):
    admins = UserSerializer(many=True)

    class Meta:
        model = Account
