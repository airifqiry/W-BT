# Generated by Django 5.1.7 on 2025-03-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_remove_userprofileinfo_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='needs',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('volunteer', 'patient')], default='patient', max_length=20),
        ),
    ]
