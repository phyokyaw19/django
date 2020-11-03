from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
import numpy
import pandas as pd
import datetime
from django.db.models.signals import post_save

class documents(models.Model):
    DEPARTMENTS = (('DC', 'DC'), ('QMS', 'QMS'), ('AD', 'AD'), ('ML', 'ML'),)
    DOC_TYPES = (('Manual', 'Manual'), ('Procedure', 'Procedure'), ('Form', 'Form'), ('WI', 'WI'), ('Others', 'Others'),)

    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True, choices=DOC_TYPES)
    rev = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True, choices=DEPARTMENTS)
    issued_date = models.DateTimeField(' in mm/dd/yyyy format (e.g. 12/31/2020)',
                                       auto_now_add=False, auto_now=False,blank=True, null=True)
    indexing_method = models.CharField(max_length=100, blank=True, null=True)
    related_procedure = models.CharField(max_length=100, blank=True, null=True)
    storage_location = models.CharField(max_length=100, blank=True, null=True)
    retention_period = models.CharField(max_length=100, blank=True, null=True)
    original_doc = models.CharField(max_length=100, blank=True, null=True)
    distributed_dept = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class external_documents(models.Model):
    DEPARTMENTS = (('DC', 'DC'), ('QMS', 'QMS'), ('AD', 'AD'), ('ML', 'ML'),)

    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    item = models.CharField(max_length=100, blank=True, null=True)
    received_date = models.DateTimeField(' in mm/dd/yyyy format (e.g. 12/31/2020)',
                                       auto_now_add=False, auto_now=False,blank=True, null=True)
    controlled_location = models.CharField(max_length=100, blank=True, null=True, choices=DEPARTMENTS)
    recorded_by = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)

def create_master_list(sender, instance, created, **kwargs):
    if created:
        target =  documents.objects.get(name='External Document List')
        rev_no = target.rev
        target.rev = int(rev_no) + 1
        target.save()
        print('Document is updated in master list')
post_save.connect(create_master_list, sender=external_documents)

