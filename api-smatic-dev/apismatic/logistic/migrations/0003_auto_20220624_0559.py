# Generated by Django 4.0.5 on 2022-06-24 05:59

from django.db import migrations
from apismatic.logistic.models import RackModel


def seed_rack(apps, schema_editor):
    RackModel.objects.create(name="A1")
    RackModel.objects.create(name="A2")


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_rackmodel_name'),
    ]

    operations = [
        migrations.RunPython(seed_rack)
    ]
