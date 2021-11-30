from django.db import models
import uuid
from django.urls import reverse


class ClientModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=55)
    email = models.EmailField("Email", max_length=100)

    def __str__(self):
        return self.name
