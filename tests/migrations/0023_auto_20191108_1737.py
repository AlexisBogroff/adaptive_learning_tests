# Generated by Django 2.2.5 on 2019-11-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0022_auto_20191108_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass_dyntest',
            name='id_test',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
