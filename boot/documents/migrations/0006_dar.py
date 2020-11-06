# Generated by Django 3.1 on 2020-11-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_remove_external_documents_current_ext_doc_rev'),
    ]

    operations = [
        migrations.CreateModel(
            name='dar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('dar_no', models.CharField(blank=True, max_length=100, null=True)),
                ('received_date', models.DateTimeField(blank=True, null=True, verbose_name='Fill date in mm/dd/yyyy format (e.g. 12/31/2020)')),
                ('purpose', models.CharField(blank=True, choices=[('DC', 'DC'), ('QMS', 'QMS'), ('AD', 'AD'), ('ML', 'ML')], max_length=100, null=True)),
                ('detail', models.CharField(blank=True, choices=[('Create New Document', 'Create New Document'), ('Update Revision', 'Update Revision')], max_length=200, null=True)),
                ('requested_by', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, max_length=100, null=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
