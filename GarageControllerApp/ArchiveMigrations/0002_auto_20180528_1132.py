# Generated by Django 2.0.5 on 2018-05-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GarageControllerApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garage_user',
            name='name',
        ),
        migrations.AddField(
            model_name='garage_user',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='garage_user',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='garage_user',
            name='middle_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='garage_user',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
