# Generated by Django 5.0.1 on 2024-02-04 07:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbr', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uuid', models.UUIDField(null=True, verbose_name='device uuid')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login date')),
                ('device_type', models.PositiveSmallIntegerField(choices=[(1, 'web'), (2, 'ios'), (3, 'android'), (4, 'pc')], default=1)),
                ('device_os', models.CharField(blank=True, max_length=20, verbose_name='device os')),
                ('device_model', models.CharField(blank=True, max_length=20, verbose_name='device model')),
                ('app_version', models.CharField(blank=True, max_length=20, verbose_name='app version')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
