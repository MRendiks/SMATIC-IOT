from django.db import models


class PermissionManager(models.Manager):
    pass


class Permission(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=64, null=False, blank=False)

    objects = PermissionManager()

    class Meta:
        app_label = 'user'
        db_table = 'permission'

    def __str__(self):
        return self.name
