# Generated by Django 5.0.7 on 2024-07-30 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_rename_appointment_billinginformation_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billinginformation',
            name='services',
        ),
    ]