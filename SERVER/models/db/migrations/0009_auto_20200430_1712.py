# Generated by Django 3.0.4 on 2020-04-30 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_commentary_cotation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.RemoveField(
            model_name='result',
            name='file',
        ),
        migrations.AddField(
            model_name='result',
            name='winner',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='db.Profile'),
        ),
    ]