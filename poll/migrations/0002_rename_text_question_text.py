# Generated by Django 4.0 on 2021-12-09 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Text',
            new_name='text',
        ),
    ]
