# Generated by Django 4.1 on 2022-10-20 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0002_visualization_abc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visualization',
            name='abc',
        ),
    ]
