from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import JobApplication

# Create your views here.


@login_required
def index(request):
    applications = JobApplication.objects.filter(user=request.user)
    context = {"applications": applications}
    return render(request, "base/index.html", context=context)


@login_required
def job_detail(request, id):
    job_application = JobApplication.objects.get(id=id)
    if job_application.user != request.user:
        return HttpResponse("You are not allowed here")
    else:
        context = {"job_application": job_application}
        return render(request, "base/htmx_components/job_details.html", context)


def get_details_homeview(request):
    return render(request, "base/htmx_components/details_homeview.html")
