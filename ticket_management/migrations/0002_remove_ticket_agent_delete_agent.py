# Generated by Django 4.2.5 on 2023-09-27 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='agent',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
    ]
