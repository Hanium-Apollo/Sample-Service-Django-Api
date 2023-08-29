from django.urls import include, path
from rest_framework import routers

from main.views import ScheduleViewSet

app_name = "main"
sechedule_router = routers.DefaultRouter(trailing_slash=False)
sechedule_router.register("schedule", ScheduleViewSet, basename="schedule")

urlpatterns = [
    path("", include(sechedule_router.urls)),
]
