# Generated by Django 4.1.7 on 2023-03-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='Stat_Value',
            field=models.IntegerField(default=1),
        ),
    ]