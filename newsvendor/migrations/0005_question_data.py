# Generated by Django 3.0.8 on 2020-08-04 21:13

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsvendor', '0004_remove_question_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='data',
            field=jsonfield.fields.JSONField(default=list),
        ),
    ]
