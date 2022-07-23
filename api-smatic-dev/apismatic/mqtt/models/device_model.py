from django.db import models


class DeviceModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=20)
    vendor = models.CharField(max_length=30)
    mac_address = models.CharField(max_length=17, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
