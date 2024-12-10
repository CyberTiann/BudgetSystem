# Generated by Django 5.1.3 on 2024-12-09 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_budget_category_annual_budget_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='annual_budget',
        ),
        migrations.RemoveField(
            model_name='funds',
            name='annual_budget',
        ),
        migrations.RemoveField(
            model_name='mooe',
            name='annual_budget',
        ),
        migrations.RemoveField(
            model_name='workgroup',
            name='workgroup',
        ),
        migrations.AddField(
            model_name='budget_category',
            name='workgroup',
            field=models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='budget_categories', to='core.workgroup'),
        ),
        migrations.AddField(
            model_name='workgroup',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='workgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='budgets', to='core.workgroup'),
        ),
        migrations.AlterField(
            model_name='funds',
            name='workgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to='core.workgroup'),
        ),
        migrations.AlterField(
            model_name='mooe',
            name='workgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mooes', to='core.workgroup'),
        ),
    ]