# Generated by Django 4.0.5 on 2022-06-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rackmodel',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
