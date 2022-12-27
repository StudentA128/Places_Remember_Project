from django.db import models


class Places(models.Model):
    place_title = models.CharField("Название", max_length=64)
    place_description = models.TextField("Комментарий")
    place_latitude = models.FloatField("Широта", default=56.0)
    place_longitude = models.FloatField("Долгота", default=92.88)
    user_id = models.CharField(max_length=64)
