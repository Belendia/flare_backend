# Generated by Django 2.2.10 on 2020-05-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20200509_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresult',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='surveyresult',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='surveyresult',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='surveyresult',
            name='session_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
