# Generated by Django 4.1 on 2022-10-20 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0005_visualization_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visualization',
            name='abc',
        ),
    ]
