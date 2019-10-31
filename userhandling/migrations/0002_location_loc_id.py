# Generated by Django 2.2.4 on 2019-10-31 00:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userhandling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='loc_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
