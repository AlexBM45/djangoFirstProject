# Generated by Django 4.0.3 on 2022-03-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_author_publisher_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Estatus'),
        ),
    ]
