# Generated by Django 3.1.1 on 2020-11-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsvendor', '0007_auto_20201117_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gamename',
            field=models.CharField(default='0000000', max_length=128),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(max_length=4000),
        ),
    ]
