# Generated by Django 2.2.7 on 2019-12-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyurl_app', '0003_longurl_ips'),
    ]

    operations = [
        migrations.AddField(
            model_name='longurl',
            name='redirectIP',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
