# Generated by Django 3.2.5 on 2021-07-16 18:16

import API.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default='', upload_to=API.models.url_book_file),
            preserve_default=False,
        ),
    ]