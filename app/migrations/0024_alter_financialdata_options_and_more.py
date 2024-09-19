# Generated by Django 5.0.6 on 2024-09-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_financialyeardata_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financialdata',
            options={'verbose_name': 'FinancialData', 'verbose_name_plural': 'FinancialData'},
        ),
        migrations.AlterModelOptions(
            name='financialdatatranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'FinancialData Translation'},
        ),
        migrations.AlterModelOptions(
            name='financialyeardata',
            options={'verbose_name': 'FinancialYearData', 'verbose_name_plural': 'FinancialYearData'},
        ),
        migrations.AlterModelOptions(
            name='license',
            options={'verbose_name': 'License', 'verbose_name_plural': 'Licenses'},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'verbose_name': 'Year', 'verbose_name_plural': 'Years'},
        ),
    ]
