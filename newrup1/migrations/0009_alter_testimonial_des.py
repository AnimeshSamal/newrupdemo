# Generated by Django 4.0.2 on 2023-08-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrup1', '0008_alter_achivement_link_alter_photo_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='des',
            field=models.TextField(max_length=300),
        ),
    ]