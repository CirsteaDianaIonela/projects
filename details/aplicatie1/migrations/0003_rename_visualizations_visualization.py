# Generated by Django 4.1 on 2022-08-19 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0002_rename_visualization_visualizations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visualizations',
            new_name='Visualization',
        ),
    ]