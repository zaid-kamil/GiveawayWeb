from django.db import models


# Create your models here.
from django.utils.timezone import now


class ContactUs(models.Model):
    name = models.CharField(max_length=55, )
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=20)
    msg = models.TextField(max_length=500)
    timestamp = models.DateTimeField(default=now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.email
