from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import external_documents, documents
from datetime import date

@receiver(post_save, sender=external_documents)
def create_master_list(sender, instance, created, **kwargs):
    if created:
        target1 = documents.objects.get(name='External Document List')
        rev_no = target1.rev
        target1.rev = int(rev_no) + 1
        target1.received_date = date.today()
        target1.save()
        print('Document is updated in master list')
    if created:
        target2 = documents.objects.get(name='Document Master List')
        rev_no = target2.rev
        target2.rev = int(rev_no) + 1
        target2.issued_date = date.today()
        target2.save()
        print('Document is updated in master list')

@receiver(post_save, sender=external_documents)
def update_master_list(sender, instance, created, **kwargs):
    if created == False:
        target1 = documents.objects.get(name='External Document List')
        rev_no = target1.rev
        target1.rev = int(rev_no) + 1
        target1.received_date = date.today()
        target1.save()
        print('Document is updated in master list')
    if created == False:
        target2 = documents.objects.get(name='Document Master List')
        rev_no = target2.rev
        target2.rev = int(rev_no) + 1
        target2.issued_date = date.today()
        target2.save()
        print('Document is updated in master list')

