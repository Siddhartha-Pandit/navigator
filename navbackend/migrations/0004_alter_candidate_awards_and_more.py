# Generated by Django 4.2.3 on 2023-07-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0003_alter_candidate_mobile_alter_candidate_nationality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='awards',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='bachelor_institute',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='bachelor_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='internsip',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='plus_two_institute',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='plus_two_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='project',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='refrence_email_1',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='refrence_email_2',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='refrence_name_1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='refrence_name_2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='refrence_phone_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='refrence_phone_2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='see_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='technical_skills',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
