from django.contrib import admin
from .models import documents, external_documents

admin.site.register(documents)
admin.site.register(external_documents)
