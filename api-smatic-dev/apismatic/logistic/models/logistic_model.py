import uuid
from django.db import models
from .rack_model import RackModel
from apismatic.user.models.user_model import User


class LogisticManager(models.Manager):
    def get_logistic_of_each_rack(self) -> list:
        racks = RackModel.objects.all()
        list_rack = []
        for rack in racks:
            logistics = list(self.filter(rack=rack).values('id', 'rfid_tag', 'owner__name'))
            list_rack.append({
                'id': rack.id,
                'name': rack.name,
                'logistics': logistics
            })
        return list_rack


class LogisticModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rfid_tag = models.CharField(max_length=16, unique=True)
    rack = models.ForeignKey(RackModel, on_delete=models.PROTECT, default=None, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    objects = LogisticManager()

    class Meta:
        app_label = "logistic"
        db_table = "logistic"
