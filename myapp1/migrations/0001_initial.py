# Generated by Django 3.2.25 on 2024-12-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animalwebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
