# Generated by Django 3.1 on 2020-09-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0005_suppliers'),
    ]

    operations = [
        migrations.AddField(
            model_name='machines',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
