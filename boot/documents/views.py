from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import documents, external_documents
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


def show_dm(request):
    revision_no = documents.objects.get(name='Document Master List')
    document = documents.objects.all().order_by('type','code');
    return render(request, 'documents/doc_master/master_list.html', {'documents': document,
                                                          'revision_no': revision_no})

class document_master_create(CreateView):
    template_name = 'documents/doc_master/document_master_create.html'
    model = documents
    fields = '__all__'
    success_url = reverse_lazy('documents:show_dm')

class document_master_detail(DetailView):
    template_name = 'documents/doc_master/document_master_detail.html'
    model = documents
    context_object_name = 'document'


class document_master_update(UpdateView):
    template_name = 'documents/doc_master/document_master_update.html'
    model = documents
    fields = '__all__'
    success_url = reverse_lazy('documents:show_dm')


class document_master_delete(DeleteView):
    template_name = 'documents/doc_master/document_master_delete.html'
    model = documents
    success_url = reverse_lazy('documents:show_dm')

#################################################################################################
def external_doc_list (request):
    target = documents.objects.get(name='External Document List')
    external_document = external_documents.objects.all().order_by('code');
    return render(request, 'documents/external_doc/external_documents_list.html', {'external_documents': external_document,
                                                                      'target':target})

class external_doc_create(CreateView):
    template_name = 'documents/external_doc/external_doc_create.html'
    model = external_documents
    fields = '__all__'
    success_url = reverse_lazy('documents:external_doc_list')

class external_doc_detail(DetailView):
    template_name = 'documents/external_doc/external_doc_detail.html'
    model = external_documents
    context_object_name = 'external_document'


class external_doc_update(UpdateView):
    template_name = 'documents/external_doc/external_doc_update.html'
    model = external_documents
    fields = '__all__'
    success_url = reverse_lazy('documents:external_doc_list')


class external_doc_delete(DeleteView):
    template_name = 'documents/external_doc/external_doc_delete.html'
    model = external_documents
    success_url = reverse_lazy('documents:external_doc_delete')
#################################################################################################
