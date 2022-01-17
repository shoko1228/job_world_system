# Generated by Django 3.2.9 on 2021-12-13 12:50

from django.db import migrations, models
import django.db.models.deletion
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211213_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='company_user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.companyuser'),
        ),
        migrations.AddField(
            model_name='user',
            name='normal_user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='users.normaluser'),
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
