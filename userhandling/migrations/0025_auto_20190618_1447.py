# Generated by Django 2.2 on 2019-06-18 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userhandling', '0024_auto_20190617_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotePreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField()),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='userhandling.Movie')),
                ('movienight', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='userhandling.MovieNightEvent')),
            ],
        ),
        migrations.DeleteModel(
            name='VoteHandler',
        ),
    ]
