# Generated by Django 3.0.4 on 2020-03-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_profil_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='picture',
            field=models.ImageField(default=False, upload_to='profil/'),
        ),
    ]