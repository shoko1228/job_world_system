# Generated by Django 3.2.9 on 2022-02-06 19:05

from django.db import migrations, models
import django.utils.timezone
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20220129_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='normaluser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
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