# Generated by Django 3.2.20 on 2023-08-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrup1', '0015_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField()),
                ('img', models.ImageField(upload_to='slider')),
            ],
        ),
    ]
