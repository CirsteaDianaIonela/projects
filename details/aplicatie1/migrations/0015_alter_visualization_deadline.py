# Generated by Django 4.1 on 2022-09-01 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0014_alter_visualization_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualization',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]