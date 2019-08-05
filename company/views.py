# filename: views.py (Django view functions)

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views import generic
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.db.models import Q
import datetime

class CompanyListView(generic.ListView):
	model=company_detail
	template_name = 'base/company_list.html'

