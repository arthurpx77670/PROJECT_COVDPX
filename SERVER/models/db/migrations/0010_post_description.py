# Generated by Django 3.0.4 on 2020-04-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=False, max_length=20),
        ),
    ]