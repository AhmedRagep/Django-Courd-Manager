from django.shortcuts import get_object_or_404, redirect, render

from webapp.models import Record
from .forms import CreateUserForm, LoginForm,AddRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Succfully Join!')
            return redirect('webapp:login')
    return render(request,'register.html',{'form':form})


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user =authenticate (request, username=username, password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request, 'Login Succfully Join!')
                return redirect('webapp:dashboard')
    return render(request,'login.html',{'form':form})


def my_logout(request):
    auth.logout(request)
    messages.warning(request, 'Logged Out!')
    return redirect('webapp:login')


@login_required(login_url='webapp:login')
def dashboard(request):
    
    records = Record.objects.all()

    return render(request,'dashboard.html',{'records':records})


@login_required(login_url='webapp:login')
def add_record(request):
    record_form = AddRecordForm()
    if request.method=='POST':
        record_form  =AddRecordForm(request.POST or None)
        if record_form.is_valid():
            record_form.save()
            messages.success(request, 'Done Add Succfully!')
            return redirect('webapp:dashboard')
    return render(request, 'add_record.html',{'record_form':record_form})




@login_required(login_url='webapp:login')
def update_record(request,pk):
    record = get_object_or_404(Record, id=pk)
    record_form = AddRecordForm(instance=record)
    if request.method=='POST':
        record_form  =AddRecordForm(request.POST or None, instance=record)
        if record_form.is_valid():
            record_form.save()
            messages.success(request, 'Done Updated Succfully!')
            return redirect('webapp:dashboard')
    return render(request, 'update_record.html',{'record_form':record_form})



@login_required(login_url='webapp:login')
def view_record(request,pk):
    record = get_object_or_404(Record, id=pk)
    return render(request,"view_record.html", {'record' : record })



@login_required(login_url='webapp:login')
def delete_record(request,pk):
  record = get_object_or_404(Record, id=pk)
  record.delete()
  messages.warning(request, 'Deleted Done!')
  return redirect('webapp:dashboard')