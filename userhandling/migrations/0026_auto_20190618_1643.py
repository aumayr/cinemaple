# Generated by Django 2.2 on 2019-06-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userhandling', '0025_auto_20190618_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votepreference',
            name='preference',
            field=models.IntegerField(blank=True),
        ),
    ]
