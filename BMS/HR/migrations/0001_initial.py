# Generated by Django 5.1.3 on 2024-12-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='annual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sources_of_funds', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sources_of_funds', models.CharField(max_length=255)),
            ],
        ),
    ]
