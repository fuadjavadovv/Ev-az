# Generated by Django 4.1 on 2022-09-05 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_alter_porpertyimage_property_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.city'),
        ),
    ]
