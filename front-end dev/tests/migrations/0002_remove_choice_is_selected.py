# Generated by Django 2.0.7 on 2019-08-13 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='is_selected',
        ),
    ]