# Generated by Django 3.1 on 2020-08-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nrc', models.CharField(blank=True, max_length=20)),
                ('weight', models.CharField(blank=True, max_length=20)),
                ('height', models.CharField(blank=True, max_length=20)),
                ('birthplace', models.CharField(blank=True, max_length=50)),
                ('education', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True)),
                ('appoint_date', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='img')),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('marital', models.CharField(blank=True, max_length=20)),
                ('address', models.TextField(blank=True)),
            ],
        ),
    ]
