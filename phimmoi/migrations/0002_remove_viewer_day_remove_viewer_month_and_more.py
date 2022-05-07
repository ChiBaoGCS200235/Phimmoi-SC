# Generated by Django 4.0.4 on 2022-05-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phimmoi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewer',
            name='day',
        ),
        migrations.RemoveField(
            model_name='viewer',
            name='month',
        ),
        migrations.RemoveField(
            model_name='viewer',
            name='year',
        ),
        migrations.AddField(
            model_name='viewer',
            name='birthday',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
