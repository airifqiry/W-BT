# Generated by Django 5.1.7 on 2025-03-22 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_settlement_userprofileinfo_assigned_patients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='needs',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='skills',
        ),
    ]
