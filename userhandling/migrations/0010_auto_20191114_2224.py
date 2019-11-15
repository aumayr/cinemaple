# Generated by Django 2.2.4 on 2019-11-15 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userhandling', '0009_auto_20191109_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationpermission',
            name='invitor',
        ),
        migrations.AddField(
            model_name='locationpermission',
            name='inviter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='locationpermission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locperms', to=settings.AUTH_USER_MODEL),
        ),
    ]
