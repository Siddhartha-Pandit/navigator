# Generated by Django 4.2.3 on 2023-07-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0018_alter_hrstaff_autonumber_alter_hrstaff_user_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrstaff',
            name='autonumber',
            field=models.CharField(default='', max_length=5, null=True),
        ),
    ]