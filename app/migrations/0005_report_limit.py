# Generated by Django 3.1.7 on 2021-03-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_report_conname'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='limit',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]