# Generated by Django 3.1 on 2020-10-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_external_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='external_documents',
            name='current_ext_doc_rev',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
