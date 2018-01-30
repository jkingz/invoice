# Generated by Django 2.0 on 2018-01-22 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20180122_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='display_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='temp',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='temp',
            name='client',
        ),
        migrations.RemoveField(
            model_name='temp',
            name='company',
        ),
    ]
