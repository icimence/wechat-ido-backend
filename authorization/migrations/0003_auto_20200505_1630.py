# Generated by Django 3.0.5 on 2020-05-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_auto_20181223_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='user',
            name='mission',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.TextField(default='[]'),
        ),
    ]
