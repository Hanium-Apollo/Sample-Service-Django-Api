from django.db import models


class schedule(models.Model):
    content = models.CharField(max_length=200)

    class Meta:
        db_table = "schedule"


# Create your models here.
