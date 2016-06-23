# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160623_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_criado',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_publicado',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
