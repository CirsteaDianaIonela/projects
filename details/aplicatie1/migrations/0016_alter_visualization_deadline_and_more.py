# Generated by Django 4.1 on 2022-09-06 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0015_alter_visualization_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualization',
            name='deadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='visualization',
            name='percentage',
            field=models.CharField(choices=[('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], default='0%', max_length=20),
        ),
    ]
