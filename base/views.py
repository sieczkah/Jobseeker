from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import JobApplication

# Create your views here.


@login_required
def index(request):
    context = {}
    return render(request, "base/index.html", context=context)
