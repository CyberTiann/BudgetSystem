# Generated by Django 5.1.3 on 2024-12-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_mooe_received_from_remove_mooe_sl_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='annual_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='percentage',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='unutilized',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='funds',
            name='annual_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='funds',
            name='percentage',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='funds',
            name='unutilized',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='mooe',
            name='annual_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='mooe',
            name='percentage',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='mooe',
            name='unutilized',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mooe',
            name='date',
            field=models.DateField(),
        ),
    ]