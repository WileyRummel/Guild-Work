# Generated by Django 2.2.7 on 2019-12-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyurl_app', '0004_longurl_redirectip'),
    ]

    operations = [
        migrations.AddField(
            model_name='longurl',
            name='url_length',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
