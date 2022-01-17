# Generated by Django 3.2.9 on 2021-12-13 20:54

from django.db import migrations, models
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20211213_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyuser',
            name='address',
            field=models.CharField(blank=True, default=0, max_length=256, verbose_name='本社所在地'),
        ),
        migrations.AlterField(
            model_name='companyuser',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
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
