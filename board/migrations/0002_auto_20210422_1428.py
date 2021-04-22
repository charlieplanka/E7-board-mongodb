# Generated by Django 3.0.5 on 2021-04-22 11:28

import board.models
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='comments',
            field=djongo.models.fields.EmbeddedField(blank=True, model_container=board.models.Comment, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=djongo.models.fields.EmbeddedField(blank=True, model_container=board.models.Tag, null=True),
        ),
    ]
