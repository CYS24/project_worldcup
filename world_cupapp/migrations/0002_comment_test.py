# Generated by Django 4.0.7 on 2022-08-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_cupapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_test',
            fields=[
                ('comment_num', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('theme', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('hit_num', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
