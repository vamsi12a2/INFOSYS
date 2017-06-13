# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from .forms import User_Form
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from .models import User
from django.forms import ModelForm

# Create your views here.
def index_view(request):
    dat = User.objects.all()
    return render(request, 'index.html',{"data":dat});

def post_view(request,id):
    instance=get_object_or_404(User,id=id)
    return render(request, 'post_details.html',{"obj":instance});

def name_view(request,name):
    instance=get_object_or_404(User,name=name)
    return render(request, 'post_details.html',{"obj":instance});


def user_form(request):
    form = User_Form(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        try:
            obj = User.objects.get(name=instance.name)
        except User.DoesNotExist:
            instance.save()
            #print "hey"
            return HttpResponseRedirect(instance.get_absolute_url())
        messages.error(request,"Name alredy exists")
        return render(request,"create_user.html",context)

    else:
        return render(request,"create_user.html",context)