# Generated by Django 5.1.3 on 2024-12-09 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_budget_annual_budget_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_category',
            name='workgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='budget_categories', to='core.workgroup'),
        ),
    ]
