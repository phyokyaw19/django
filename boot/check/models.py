from django.db import models
from django.contrib.auth.models import User

class Staffs(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    nrc = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    height = models.CharField(max_length=20, blank=True)
    birthplace = models.CharField(max_length=50, blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    appoint_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='img', blank=True)
    phone = models.CharField(max_length=50, blank=True)
    marital = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length = 250, null = True, blank = True)

    class Profile(models.Model):
        date_of_birth = models.DateField()

        def age(self):
            import datetime
            dob = self.date_of_birth
            tod = datetime.date.today()
            my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
            return my_age

    def __str__(self):
        return self.name