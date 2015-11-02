from rest_framework2 import serializers
from tests.models import NullableForeignKeySource


class NullableFKSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NullableForeignKeySource
