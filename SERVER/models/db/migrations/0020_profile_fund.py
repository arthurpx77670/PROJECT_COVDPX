# Generated by Django 3.0.4 on 2020-05-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0019_profile_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fund',
            field=models.FloatField(default=0),
        ),
    ]