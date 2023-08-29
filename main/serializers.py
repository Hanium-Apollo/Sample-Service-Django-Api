from rest_framework import serializers
from .models import schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = schedule
        fields = ["id", "content"]
        read_only_fields = ["id"]
