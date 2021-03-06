# Generated by Django 2.1a1 on 2018-05-28 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Controller_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('device_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Door_Controller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number', models.TextField(blank=True, null=True)),
                ('street', models.TextField(blank=True, null=True)),
                ('locality', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('uniqueID', models.CharField(max_length=20)),
                ('device_Online', models.IntegerField(default=False)),
                ('create_date', models.DateTimeField()),
                ('ip_address', models.TextField()),
                ('device_port', models.IntegerField()),
                ('controller_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GarageControllerApp.Controller_Type')),
                ('device_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
