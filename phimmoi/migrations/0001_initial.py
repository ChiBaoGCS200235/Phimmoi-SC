# Generated by Django 4.0.4 on 2022-05-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=200)),
                ('chapter', models.IntegerField(max_length=1000)),
                ('video', models.TextField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=200)),
                ('chapter', models.IntegerField(max_length=100)),
                ('totalChapter', models.IntegerField(max_length=100)),
                ('views', models.IntegerField(max_length=1000000)),
                ('description', models.TextField(max_length=1000)),
                ('openingSong', models.TextField(max_length=100)),
                ('closingSong', models.TextField(max_length=100)),
                ('movieLink', models.TextField(default='', max_length=1000)),
                ('picture', models.TextField(default='', max_length=100)),
                ('background', models.TextField(default='', max_length=100)),
                ('type', models.TextField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('repassword', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=200, null=True)),
                ('fullname', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('day', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, default='', max_length=5, null=True)),
            ],
        ),
    ]
