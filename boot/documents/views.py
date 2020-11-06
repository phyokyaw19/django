from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import documents, external_documents, dar
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

def list_compact(request):
    return render(request, 'documents/doc_master/master_list_compact.html')

def show_dm(request):
    revision_no = documents.objects.get(name='Document Master List')
    document = documents.objects.all().order_by('type','code');
    return render(request, 'documents/doc_master/master_list.html', {'documents': document,
                                                          'revision_no': revision_no})

def show_dm_print_view(request):
    revision_no = documents.objects.get(name='Document Master List')
    document = documents.objects.all().order_by('type','code');
    return render(request, 'documents/doc_master/master_list_print.html', {'documents': document,
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

def external_doc_list_print (request):
    target = documents.objects.get(name='Document Action Request (DAR)')
    external_doc = external_documents.objects.all().order_by('code');
    return render(request, 'documents/dar/dar_list_print.html', {'external_doc': external_doc,
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

def dar_list (request):
    target = documents.objects.get(name='Document Action Request (DAR)')
    dar1 = dar.objects.all().order_by('code');
    return render(request, 'documents/dar/dar_list.html', {'dar': dar1,
                                                                      'target':target})
def dar_list_print (request):
    target = documents.objects.get(name='Document Action Request (DAR)')
    dar1 = dar.objects.all().order_by('code');
    return render(request, 'documents/dar/dar_list_print.html', {'dar': dar1,
                                                                      'target':target})

class dar_create(CreateView):
    template_name = 'documents/dar/dar_create.html'
    model = dar
    fields = '__all__'
    success_url = reverse_lazy('documents:dar_list')

class dar_detail(DetailView):
    template_name = 'documents/dar/dar_detail.html'
    model = dar
    context_object_name = 'dar'


class dar_update(UpdateView):
    template_name = 'documents/dar/dar_update.html'
    model = dar
    fields = '__all__'
    success_url = reverse_lazy('documents:dar_list')


class dar_delete(DeleteView):
    template_name = 'documents/dar/dar_delete.html'
    model = dar
    success_url = reverse_lazy('documents:dar_delete')
#################################################################################################

