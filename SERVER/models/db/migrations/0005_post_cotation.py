# Generated by Django 3.0.4 on 2020-04-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_remove_profile_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cotation',
            field=models.IntegerField(null=True),
        ),
    ]