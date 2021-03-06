# Generated by Django 3.2.9 on 2022-03-21 17:52

from django.db import migrations, models
import django.db.models.deletion
import ulid.api.api


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220321_1752'),
        ('recruit', '0008_auto_20220319_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comfavoriteusermodel',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=125, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userfavoriteitemmodel',
            name='id',
            field=models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='MatchingrModel',
            fields=[
                ('id', models.CharField(default=ulid.api.api.Api.new, editable=False, max_length=32, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('delete_flg', models.IntegerField(blank=True, default=0, verbose_name='削除フラグ')),
                ('com_user', models.ForeignKey(db_column='com_user_id', on_delete=django.db.models.deletion.CASCADE, to='users.companyuser', verbose_name='企業')),
                ('normal_user', models.ForeignKey(db_column='normal_user_id', on_delete=django.db.models.deletion.CASCADE, to='users.normaluser', verbose_name='求職者')),
            ],
            options={
                'verbose_name': 'マッチング',
                'verbose_name_plural': 'マッチング',
                'db_table': 'matching',
            },
        ),
    ]
