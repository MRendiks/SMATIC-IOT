# Generated by Django 4.0.5 on 2022-06-23 09:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('permissions', models.ManyToManyField(to='user.permission')),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=24)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.role')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
