from django.contrib import admin

from .models import Company, JobOffer

# Register your models here.
admin.site.register(JobOffer)
admin.site.register(Company)
