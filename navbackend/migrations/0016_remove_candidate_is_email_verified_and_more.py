# Generated by Django 4.2.3 on 2023-07-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0015_hrstaff_is_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='is_email_verified',
        ),
        migrations.RemoveField(
            model_name='hrstaff',
            name='is_email_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
