# Generated by Django 4.2.3 on 2023-07-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0004_alter_candidate_awards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='see_marks',
            field=models.IntegerField(default=0, null=True),
        ),
    ]