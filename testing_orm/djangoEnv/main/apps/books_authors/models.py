# Inside models.py
from __future__ import unicode_literals
from django.db import models

class Books(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
class Authors(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.TextField(null=True, blank=True)
  email = models.CharField(max_length=255)
  # notes = models.TextField(default= " ")
  book = models.ManyToManyField(Books, related_name="authors")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
