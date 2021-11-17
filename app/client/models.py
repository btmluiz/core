from django.db import models


class ClientModel(models.Model):

    uui = models.UUIDField("ID")
    name = models.CharField("Name", max_length=55)
    email = models.EmailField("Email", max_length=100)

    def __str__(self):
        return self.name
