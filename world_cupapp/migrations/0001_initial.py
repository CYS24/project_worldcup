# Generated by Django 4.0.7 on 2022-08-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('url', models.TextField()),
                ('win_num', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Brand_member',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('rdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rank', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('content', models.TextField()),
                ('name', models.TextField(max_length=128)),
                ('date', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
    ]