# Generated by Django 4.2.3 on 2023-07-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbackend', '0012_alter_candidate_gender_alter_candidate_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='awards',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='bachelor_institute',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='bachelor_marks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='bachelor_transcript',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='internsip',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='nationality',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='permanentaddress',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='plus_two_institute',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='plus_two_marks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='plus_two_transcript',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='static/image/'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='project',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='refrence_email_1',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='refrence_email_2',
            field=models.EmailField(default='', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='refrence_name_1',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='refrence_name_2',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='refrence_phone_1',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='refrence_phone_2',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='see_institute',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='see_marks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='see_transcript',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='technical_skills',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='temporaryaddress',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]