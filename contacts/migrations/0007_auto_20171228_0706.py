# Generated by Django 2.0 on 2017-12-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20171228_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Miss.', 'Miss.'), ('Dr.', 'Dr.')], max_length=5, null=True),
        ),
    ]