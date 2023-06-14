from typing import Any, Dict, Optional

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms.models import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from utils import openai_jobassistant

from .models import JobOffer


@login_required
def ai_jobassistant_view(request, pk):
    offer = JobOffer.objects.get(id=pk)

    if request.user == offer.user:
        posistion = offer.posistion
        description = offer.description
        assistant = openai_jobassistant.JobAssistant(posistion, description)
        request_status = assistant.send_request()

        if request_status == "200":
            ai_response = assistant.get_styled_answer()
            offer.ai_generated_data = ai_response
            offer.save()
            return redirect(reverse_lazy("joboffer-detail", args=[offer.id]))
        else:
            return HttpResponse(request_status)

    else:
        return Http404


class JobOfferList(LoginRequiredMixin, ListView):
    model = JobOffer
    context_object_name = "job_offers"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["job_offers"] = context["job_offers"].filter(user=self.request.user)

        search_input = self.request.GET.get("search") or ""
        if search_input:
            context["job_offers"] = context["job_offers"].filter(
                Q(company__icontains=search_input)
                | Q(posistion__icontains=search_input)
            )
        context["search_input"] = search_input
        return context


class HomeView(JobOfferList):
    template_name = "base/index.html"


class JobOfferDetail(LoginRequiredMixin, DetailView):
    model = JobOffer
    context_object_name = "job_offer"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


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

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class JobOfferDelete(LoginRequiredMixin, DeleteView):
    model = JobOffer
    context_object_name = "job_offer"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
