# Generated by Django 2.0 on 2018-01-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20180109_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_display_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
