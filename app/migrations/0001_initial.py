# Generated by Django 3.0.2 on 2021-02-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('file_csv', models.FileField(upload_to='csv_file/')),
            ],
            options={
                'db_table': 'Csv',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('pin', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('imei', models.CharField(blank=True, max_length=100)),
                ('signal', models.CharField(blank=True, max_length=100)),
                ('report', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'Device',
            },
        ),
        migrations.CreateModel(
            name='Num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('finame', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Num',
            },
        ),
        migrations.CreateModel(
            name='Numupdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Numupdate',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('pin', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'db_table': 'Report',
            },
        ),
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Sim',
            },
        ),
        migrations.CreateModel(
            name='Spin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=50)),
                ('sim', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Spin',
            },
        ),
    ]
