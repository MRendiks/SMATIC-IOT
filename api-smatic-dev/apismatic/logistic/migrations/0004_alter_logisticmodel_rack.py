# Generated by Django 4.0.5 on 2022-06-24 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0003_auto_20220624_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticmodel',
            name='rack',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='logistic.rackmodel'),
        ),
    ]