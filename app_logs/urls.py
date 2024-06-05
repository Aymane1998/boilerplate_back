from rest_framework import routers
from django.urls import path
from app_logs import views


app_name = "logs"

router = routers.SimpleRouter()


urlpatterns = [
    path("<str:model>/", views.LogsViews.as_view(), name="logs"),
]

urlpatterns += router.urls
