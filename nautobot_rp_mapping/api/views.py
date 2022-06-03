from rest_framework.viewsets import ModelViewSet

from .. import models
from .serializers import StaticRPSerializer, RPGroupEntrySerializer


class StaticRPViewSet(ModelViewSet):
    queryset = models.StaticRP.objects.prefetch_related("tags")
    serializer_class = StaticRPSerializer


class RPGroupEntryViewSet(ModelViewSet):
    queryset = models.RPGroupEntry.objects.prefetch_related("tags")
    serializer_class = RPGroupEntrySerializer
