from django.db import models

class RackModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)

    class Meta:
        app_label = "logistic"
        db_table = "rack"
