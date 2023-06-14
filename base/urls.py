from django.urls import path

from .views import (
    HomeView,
    JobOfferCreate,
    JobOfferDelete,
    JobOfferDetail,
    JobOfferList,
    JobOfferUpdate,
    ai_jobassistant_view,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("list", JobOfferList.as_view(), name="joboffer-list"),
    path("offer/<str:pk>/", JobOfferDetail.as_view(), name="joboffer-detail"),
    path("update/<str:pk>/", JobOfferUpdate.as_view(), name="joboffer-update"),
    path("delete/<str:pk>/", JobOfferDelete.as_view(), name="joboffer-delete"),
    path("get-ai-offer/<str:pk>/", ai_jobassistant_view, name="get-ai-offer"),
    path("new", JobOfferCreate.as_view(), name="joboffer-create"),
]
