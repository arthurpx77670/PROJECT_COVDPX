# Generated by Django 3.0.4 on 2020-04-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_post_cotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cotationUser',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='priceUser',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cotation',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]