# Generated by Django 3.0.2 on 2021-02-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='port',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='sim',
            name='port',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='num',
            name='content',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='num',
            name='finame',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='numupdate',
            name='mobile',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='numupdate',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='msg',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='report',
            name='num',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='sim',
            name='pin',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='spin',
            name='port',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='spin',
            name='sim',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
