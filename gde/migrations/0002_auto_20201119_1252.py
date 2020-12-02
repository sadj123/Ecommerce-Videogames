# Generated by Django 3.1.2 on 2020-11-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gde', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatcher',
            name='blood_type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dispatcher',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dispatcher',
            name='plate',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='dispatcher',
            name='rh_type',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], max_length=20),
        ),
        migrations.AlterField(
            model_name='dispatcher',
            name='telephone',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='dispatcher',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]