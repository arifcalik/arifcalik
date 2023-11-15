from django.db import models

class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length = 100, default="info@circusrestaurant.se")
