from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
import numpy
import pandas as pd
import datetime


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

    def get_date(self):
        return self.issued_date.date()

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
    def get_date(self):
        return self.received_date.date()

class dar(models.Model):
    DEPARTMENTS = (('DC', 'DC'), ('QMS', 'QMS'), ('AD', 'AD'), ('ML', 'ML'),)
    DOC_TYPES = (('Manual', 'Manual'), ('Procedure', 'Procedure'), ('Form', 'Form'), ('WI', 'WI'), ('Others', 'Others'),)
    PURPOSE = (('Create New Document', 'Create New Document'), ('Update Revision', 'Update Revision'),)

    name = models.CharField('Doc.Name (Filled by request person)',max_length=100, blank=True, null=True)
    code = models.CharField('Doc.Code (Filled by request person)',max_length=100, blank=True, null=True)
    received_date = models.DateTimeField('Fill date in mm/dd/yyyy format (e.g. 12/31/2020)(Filled by request person)',
                                       auto_now_add=False, auto_now=False,blank=True, null=True)
    purpose = models.CharField('Request Purpose (Filled by request person)',max_length=100, blank=True, null=True, choices=PURPOSE)
    detail = models.CharField('Request Detail (Filled by request person)',max_length=200, blank=True, null=True)
    requested_by = models.CharField('Requested Person (Filled by request person)',max_length=100, blank=True, null=True)
    dar_no = models.CharField('Requested Person (Filled by DC)',max_length=100, blank=True, null=True)
    approved_by = models.CharField('Approved Person (Filled by DC)',max_length=100, blank=True, null=True)
    remark = models.CharField('Remark (Filled by DC)',max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    def get_date(self):
        return self.received_date.date()






