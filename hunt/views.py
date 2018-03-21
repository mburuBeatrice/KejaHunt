# from . models import 
# from .forms import 
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')