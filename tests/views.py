from rest_framework2 import generics
from .models import NullableForeignKeySource
from .serializers import NullableFKSourceSerializer


class NullableFKSourceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = NullableForeignKeySource
    model_serializer_class = NullableFKSourceSerializer
