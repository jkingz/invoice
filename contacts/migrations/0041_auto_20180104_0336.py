# Generated by Django 2.0 on 2018-01-04 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0040_auto_20180104_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='add_more_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.AddMoreField'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='additional_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.AdditionalAddress'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.BillingAddress'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.ContactPerson'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.ShippingAddress'),
        ),
    ]