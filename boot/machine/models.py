from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
import numpy
import pandas
import datetime

class Suppliers(models.Model):
    company = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.TextField(blank=False, null=True)
    contact_phone = models.IntegerField(blank=True, null=True)
    document = models.FileField(upload_to='media/suppliers/', null=True)
    remark = models.TextField(blank=False, null=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.company


# Create your models here.
class machines(models.Model):
    INTERVAL_CHOICES = ((1, 'Day(s)'), (2, 'Week(s)'), (3, 'Month(s)'), (4, 'Year(s)'),)
    NUMBER_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'),
                       (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'),)

    title = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    serial = models.CharField(max_length=100, blank=True, null=True)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, null=True)
    body = models.TextField(blank=False, null=True)

    qc_plan_number = models.IntegerField('QC is needed in every',
                                           blank=False, null=True, choices=NUMBER_CHOICES)
    qc_plan_interval = models.IntegerField('',
                                             blank=False, null=True, choices=INTERVAL_CHOICES)

    cali_plan_number = models.IntegerField('Calibration or PM need is needed in every',
                                           blank=False, null=True, choices=NUMBER_CHOICES)
    cali_plan_interval = models.IntegerField('',
                                    blank=False, null=True, choices=INTERVAL_CHOICES)



    date = models.DateTimeField('start operating date: (mm/dd/yyyy) e.g. 12/31/2020', auto_now_add=False,
                                auto_now=False, blank=True, null=True)
    op_duration = models.DateTimeField('operation plan will be made until: (mm/dd/yyyy) e.g. 12/31/2020',
                                       auto_now_add=False, auto_now=False,blank=True, null=True)

    thumb = models.ImageField(default='default.png', blank=True)
    document = models.FileField(upload_to='media/machines/' , null=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE,)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


    def plan_dates(self):
        if self.cali_plan_interval == 1:
            a = self.date
            b = self.op_duration
            c = str(self.cali_plan_number)+'D'
            dt = pandas.date_range(start=a, end=b, freq=c)
            #my_list = []
            #for e in dt.strftime('__%B. %d, %Y__'):
                #my_list.append(e)
            return dt
        elif self.cali_plan_interval == 2:
            a = self.date
            b = self.op_duration
            c = str(self.cali_plan_number)+'W'
            dt = pandas.date_range(start=a, end=b, freq=c)
            # my_list = []
            # for e in dt.strftime('__%B. %d, %Y__'):
            # my_list.append(e)
            return dt
        elif self.cali_plan_interval == 3:
            a = self.date
            b = self.op_duration
            c = str(self.cali_plan_number)+'MS'
            dt = pandas.date_range(start=a, end=b, freq=c)
            # my_list = []
            # for e in dt.strftime('__%B. %d, %Y__'):
            # my_list.append(e)
            return dt
        else:
            a = self.date
            b = self.op_duration
            c = str(self.cali_plan_number)+'Y'
            dt = pandas.date_range(start=a, end=b, freq=c)
            # my_list = []
            # for e in dt.strftime('__%B. %d, %Y__'):
            # my_list.append(e)
            return dt

    def alert_day0(self):
        dt = self.plan_dates()
        dt_onlydate = dt.strftime('%B. %d, %Y')
        target_day = pandas.to_datetime(['today'], utc=True)
        target_day_onlydate = target_day.strftime('%B. %d, %Y')
        for alert in dt_onlydate:
            if alert == target_day_onlydate:
                return 'today is calibration date.'
            else:
                return ''

    def alert_day1(self):
        dt = self.plan_dates()
        dt_onlydate = dt.strftime('%B. %d, %Y')
        target_day = pandas.to_datetime(['today'], utc=True) + pandas.Timedelta(days = 1)
        target_day_onlydate = target_day.strftime('%B. %d, %Y')
        for alert in dt_onlydate:
            if alert == target_day_onlydate:
                return 'calibration is needed in 1 day.'
            else:
                return ''

    def alert_day2(self):
        dt = self.plan_dates()
        dt_onlydate = dt.strftime('%B. %d, %Y')
        target_day = pandas.to_datetime(['today'], utc=True) + pandas.Timedelta(days=2)
        target_day_onlydate = target_day.strftime('%B. %d, %Y')
        for alert in dt_onlydate:
            if alert == target_day_onlydate:
                return 'calibration is needed in 2 day.'
            else:
                return ''

    def alert_day3(self):
        dt = self.plan_dates()
        dt_onlydate = dt.strftime('%B. %d, %Y')
        target_day = pandas.to_datetime(['today'], utc=True) + pandas.Timedelta(days=3)
        target_day_onlydate = target_day.strftime('%B. %d, %Y')
        for alert in dt_onlydate:
            if alert == target_day_onlydate:
                return 'calibration is needed in 3 day.'
            else:
                return ''








