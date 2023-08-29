from rest_framework import viewsets, mixins
from .serializers import ScheduleSerializer
from .models import Schedule


class ScheduleViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
