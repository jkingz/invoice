# Generated by Django 2.0 on 2018-01-30 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_company'),
        ('invoices', '0004_auto_20180126_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Company'),
        ),
    ]
