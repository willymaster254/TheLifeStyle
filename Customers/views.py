from ast import Return
from contextlib import redirect_stderr
from urllib import request
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def massage(request):
    return render(request, 'service.html')

def Customer(request):
	
	
	form = CustomerForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ("/success/")

	context = {'form':form}
	return render(request, 'CustomerForm.html', context)
    

# def CustomerList(request):
#     context = {'customer': Customer.objects.all()}
#     return render(request, "CustomerList.html", context)
def CustomerDelete(request):
    return render(request, 'CustomerDelete.html')

def success(request):
	return render(request, 'success.html')
