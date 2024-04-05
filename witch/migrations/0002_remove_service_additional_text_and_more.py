# Generated by Django 5.0.4 on 2024-04-05 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='additional_text',
        ),
        migrations.AddField(
            model_name='service',
            name='additional_texts',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=datetime.datetime(2024, 4, 5, 15, 34, 13, 479425, tzinfo=datetime.timezone.utc), upload_to='services/'),
            preserve_default=False,
        ),
    ]
