from django.urls import path

from .views import (  # JobOfferCreate,; JobOfferUpdate,
    HomeView,
    JobOfferDelete,
    JobOfferDetail,
    JobOfferList,
    ai_jobassistant_view,
    create_JobOffer,
    update_JobOffer,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("list", JobOfferList.as_view(), name="joboffer-list"),
    path("offer/<str:pk>/", JobOfferDetail.as_view(), name="joboffer-detail"),
    path("new", create_JobOffer, name="joboffer-create"),
    path("update/<str:pk>/", update_JobOffer, name="joboffer-update"),
    path("delete/<str:pk>/", JobOfferDelete.as_view(), name="joboffer-delete"),
    path("get-ai-offer/<str:pk>/", ai_jobassistant_view, name="get-ai-offer"),
]
