# Generated by Django 3.2.11 on 2022-01-07 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0054_vlangroup_min_max_vids'),
        ('dcim', '0149_inventoryitem_templates'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='vrf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interfaces', to='ipam.vrf'),
        ),
    ]
