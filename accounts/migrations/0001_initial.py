# Generated by Django 3.2.7 on 2021-09-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('userid', models.CharField(blank=True, db_column='userId', max_length=45, null=True)),
                ('userpw', models.CharField(blank=True, db_column='userPw', max_length=45, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
    ]
