# Generated by Django 4.0 on 2021-12-16 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_view', '0002_remove_data_view_ident'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_view',
            old_name='prix_HT',
            new_name='prix_ht',
        ),
        migrations.RenameField(
            model_name='data_view',
            old_name='prix_m2_HT',
            new_name='prix_m2_ht',
        ),
        migrations.RenameField(
            model_name='data_view',
            old_name='prix_m2_TTC',
            new_name='prix_m2_ttc',
        ),
    ]
