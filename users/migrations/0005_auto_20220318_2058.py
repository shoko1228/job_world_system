# Generated by Django 3.2.9 on 2022-03-18 20:58

from django.db import migrations, models
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220318_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyuser',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='change_job_time',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='希望入社時期'),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]
