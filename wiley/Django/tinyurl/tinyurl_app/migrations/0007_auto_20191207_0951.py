# Generated by Django 2.2.7 on 2019-12-07 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tinyurl_app', '0006_auto_20191206_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='longurl',
            old_name='url_length',
            new_name='url_bits',
        ),
    ]