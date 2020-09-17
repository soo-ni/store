# Generated by Django 3.1.1 on 2020-09-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.FileField(upload_to='')),
                ('abstract', models.TextField(default=None)),
                ('key', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Summary_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_kor', models.CharField(max_length=300)),
                ('title_eng', models.CharField(blank=True, max_length=300)),
                ('main_author', models.CharField(max_length=100)),
                ('sub_author', models.TextField()),
                ('journal_kor', models.CharField(max_length=100)),
                ('journal_eng', models.CharField(max_length=100)),
                ('issuer_kor', models.CharField(max_length=100)),
                ('issuer_eng', models.CharField(max_length=100)),
                ('issue_year', models.IntegerField(default=0)),
                ('book_num', models.IntegerField(default=0)),
                ('keyword_kor', models.TextField()),
                ('keyword_eng', models.TextField()),
                ('subject', models.CharField(max_length=50)),
                ('quote', models.IntegerField(default=0)),
                ('direct_urls', models.URLField()),
                ('doi', models.CharField(max_length=50)),
                ('abstract', models.TextField()),
                ('page_num', models.IntegerField(default=0)),
            ],
        ),
    ]