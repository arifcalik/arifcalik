from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Customer

def index(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())

def AppTwo(request):
  customers = Customer.objects.all().values()
  template = loader.get_template('bookings.html')
  return HttpResponse(template.render({'customers': customers,}, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))  

def addrecord(request):
  firstname = request.POST['first']
  lastname = request.POST['last']
  email = request.POST.get('email', "info@circusrestaurant.se")
  customer = Customer(first_name=firstname, last_name=lastname, email=email)
  customer.save()
  return HttpResponseRedirect(reverse('add'))

