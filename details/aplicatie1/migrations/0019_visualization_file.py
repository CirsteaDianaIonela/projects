# Generated by Django 4.1 on 2022-09-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0018_remove_visualization_today'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualization',
            name='file',
            field=models.FileField(default='To be added', upload_to='documents/'),
        ),
    ]
