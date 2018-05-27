# Generated by Django 2.0.5 on 2018-05-27 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Controller_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Door_Controller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('street', models.TextField(blank=True, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('uniqueID', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(verbose_name='date added')),
                ('controller_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GarageControllerApp.Controller_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Garage_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email_address', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]
