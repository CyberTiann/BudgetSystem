# Generated by Django 5.1.3 on 2024-12-09 07:05

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_budget_annual_budget_budget_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget_category',
            name='annual_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='budget_category',
            name='percentage',
            field=models.FloatField(default=0.0, editable=False),
        ),
        migrations.AddField(
            model_name='budget_category',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='budget_category',
            name='unutilized',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='funds',
            name='budget_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.budget_category'),
        ),
    ]
