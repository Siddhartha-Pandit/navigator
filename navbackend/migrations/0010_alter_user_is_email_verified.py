# Generated by Django 4.2.3 on 2023-07-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0009_user_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
