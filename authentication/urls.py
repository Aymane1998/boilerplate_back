from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

app_name = 'authentication'


urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token-obtain-pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token-refresh')
]
