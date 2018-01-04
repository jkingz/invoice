# Generated by Django 2.0 on 2017-12-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0020_auto_20171228_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attention', models.CharField(blank=True, max_length=40, null=True)),
                ('street_1', models.CharField(blank=True, max_length=100, null=True)),
                ('street_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('fax', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]