# Generated by Django 3.0.4 on 2020-03-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20200330_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default=False, upload_to='file/'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='picture',
            field=models.ImageField(default=False, upload_to='picture/'),
        ),
    ]
