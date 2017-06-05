# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User
# Create your views here.
def index_view(request):
    dat = User.objects.all()
    return render(request, 'index.html',{"data":dat});
