from typing import Any, Dict

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import JobOffer


class JobOfferList(LoginRequiredMixin, ListView):
    model = JobOffer
    context_object_name = "job_offers"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["job_offers"] = context["job_offers"].filter(user=self.request.user)

        return context


class HomeView(JobOfferList):
    template_name = "base/index.html"


class JobOfferDetail(LoginRequiredMixin, DetailView):
    model = JobOffer
    context_object_name = "job_offer"


class JobOfferCreate(LoginRequiredMixin, CreateView):
    model = JobOffer
    fields = ["link", "posistion", "company", "description", "status", "salary"]
    success_url = reverse_lazy("home")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(JobOfferCreate, self).form_valid(form)


class JobOfferUpdate(LoginRequiredMixin, UpdateView):
    model = JobOffer
    fields = ["link", "posistion", "company", "description", "status", "salary"]
    success_url = reverse_lazy("home")


class JobOfferDelete(LoginRequiredMixin, DeleteView):
    model = JobOffer
    context_object_name = "job_offer"
    success_url = reverse_lazy("home")
