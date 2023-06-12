from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
]

htmx_urlpatterns = [path("job-details/<str:id>/", views.job_detail, name="job-details")]

urlpatterns += htmx_urlpatterns
