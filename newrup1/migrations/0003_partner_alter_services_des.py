# Generated by Django 4.0.2 on 2023-08-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newrup1', '0002_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.AlterField(
            model_name='services',
            name='des',
            field=models.TextField(),
        ),
    ]
