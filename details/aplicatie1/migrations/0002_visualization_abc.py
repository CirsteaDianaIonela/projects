# Generated by Django 4.1 on 2022-10-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualization',
            name='abc',
            field=models.CharField(default='Empty', max_length=100),
        ),
    ]