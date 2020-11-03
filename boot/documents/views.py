from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import documents
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


def show_dm(request):
    document = documents.objects.all().order_by('type','code');
    return render(request, 'documents/master_list.html', {'documents': document})
