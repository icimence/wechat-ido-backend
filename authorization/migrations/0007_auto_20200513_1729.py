# Generated by Django 3.0.5 on 2020-05-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_remove_user_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collection',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.TextField(default='[]'),
        ),
    ]
