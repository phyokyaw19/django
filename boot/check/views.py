from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Staffs
from django.contrib.auth.decorators import login_required
from . import forms


def check_view(request):
    return render(request, 'check/hello.html')


def add_staff(request):
    if request.method == 'POST':
        form = forms.AddStaff(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('check:check')
    else:
        form = forms.AddStaff()
    return render(request, 'check/add_staff.html', { 'form': form })

def list_staff(request):
   staffs = Staffs.objects.all().order_by('name');
   return render(request, 'check/staff_list.html', { 'staffs': staffs })

def detail_staff(request, slug):
    # return HttpResponse(slug)
    staffs = Staffs.objects.get(slug=slug)
    return render(request, 'check/detail_staff.html', { 'staffs': staffs })



