# Generated by Django 3.0.4 on 2020-04-04 08:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('receiver', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='db.Profil')),
            ],
        ),
    ]