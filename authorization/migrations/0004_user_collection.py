# Generated by Django 3.0.5 on 2020-05-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_auto_20200505_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collection',
            field=models.TextField(default='[]'),
        ),
    ]
