# Generated by Django 4.0.2 on 2023-08-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrup1', '0012_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivement',
            name='link',
            field=models.URLField(blank=True, default='', max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='link',
            field=models.URLField(blank=True, default='', max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, default='', max_length=500, unique=True),
        ),
    ]
