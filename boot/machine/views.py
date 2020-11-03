from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import machines, Suppliers
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

#def add_machine(request):
 #       if request.method == 'POST':
 #               form = forms.addmachine(request.POST, request.FILES)
 #               if form.is_valid():
 #                       # save article to db
  #                      instance = form.save(commit=False)
  #                      instance.author = request.user
  #                      instance.save()
  #                      return redirect('machine:list_machine')
  #      else:
  #              form = forms.addmachine()
   #             return render(request, 'machine/add_machine.html',{'form': form })

class MachineCreate(CreateView):
        template_name = 'machine/add_machine.html'
        model = machines
        fields = '__all__'
        success_url = reverse_lazy('machine:list_machine')


def list_machine(request):
        machine = machines.objects.all().order_by('add_date');
        return render(request, 'machine/machine_list.html', {'machines': machine})

class detail_machine(DetailView):
        template_name = 'machine/machine_detail.html'
        model = machines
        context_object_name = 'machine'

class update_machine(UpdateView):
        template_name = 'machine/machine_update.html'
        model = machines
        fields = '__all__'
        success_url = reverse_lazy('machine:list_machine')

class delete_machine(DeleteView):
        template_name = 'machine/machine_confirm_delete.html'
        model = machines
        success_url = reverse_lazy('machine:list_machine')

class SuppliersCreate(CreateView):
        template_name = 'machine/supplier_create.html'
        model = Suppliers
        fields = '__all__'
        success_url = reverse_lazy('machine:list_supplier')

def list_supplier(request):
        supplier = Suppliers.objects.all().order_by('add_date');
        return render(request, 'machine/supplier_list.html', {'suppliers': supplier})

class detail_supplier(DetailView):
        template_name = 'machine/supplier_detail.html'
        model = Suppliers
        context_object_name = 'supplier'

class update_supplier(UpdateView):
        template_name = 'machine/supplier_update.html'
        model = Suppliers
        fields = '__all__'
        success_url = reverse_lazy('machine:list_supplier')

class delete_supplier(DeleteView):
        template_name = 'machine/supplier_confirm_delete.html'
        model = Suppliers
        success_url = reverse_lazy('machine:list_supplier')