# Generated by Django 3.0.4 on 2020-05-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0015_profile_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nummber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='win',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
