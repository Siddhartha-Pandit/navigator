# Generated by Django 4.2.3 on 2023-07-27 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0024_selected'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='selected',
            new_name='isselected',
        ),
    ]
