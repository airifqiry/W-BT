# Generated by Django 5.1.7 on 2025-03-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_alter_userprofileinfo_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('volunteer', 'patient')], default='patient', max_length=10),
            preserve_default=False,
        ),
    ]
