from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest.serializer.eavserializer import ValueSerializer
from rest.models.eav_typed_column import Value


class ListCreateValueView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ValueSerializer
    queryset = Value.objects.all()
