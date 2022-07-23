from django.db import models
from .permission_model import Permission


class Role(models.Model):
    LOGISTIC_OWNER_ID = 1
    WAREHOUSE_EMPLOYEE_ID = 2
    WAREHOUSE_OWNER_ID = 3

    LOGISTIC_OWNER_NAME = 'LOGISTIC_OWNER'
    WAREHOUSE_EMPLOYEE_NAME = 'WAREHOUSE_EMPLOYEE'
    WAREHOUSE_OWNER_NAME = 'WAREHOUSE_OWNER'

    id = models.PositiveSmallIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=64, null=False, blank=False)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        app_label = 'user'
        db_table = 'role'
