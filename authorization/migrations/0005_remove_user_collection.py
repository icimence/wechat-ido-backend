# Generated by Django 3.0.5 on 2020-05-13 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_user_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='collection',
        ),
    ]