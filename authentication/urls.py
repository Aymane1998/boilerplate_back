from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (MyTokenObtainPairView,
                    CurrentUserView,
                    UserListCreateView,
                    UserUpdateView,
                    UserDeleteView,
                    UserDetailView,
                    ServiceListCreateView,
                    ServiceDetailView,
                    ServiceUpdateView,
                    ServiceDeleteView,
                    UniteListCreateView,
                    DepartementListCreateView,
                    DepartementUpdateView,
                    DepartementDetailView)

app_name = 'authentication'


urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token-obtain-pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token-refresh'),
    path('current-user/', CurrentUserView.as_view(), name="current-user"),

    path('user/', UserListCreateView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    path('service/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),

    path('unite/', UniteListCreateView.as_view(), name='unite-list-create'),

    path('departement/', DepartementListCreateView.as_view(), name='departement-list-create'),
    path('departement/<int:pk>/', DepartementUpdateView.as_view(), name='departement-update'),
    path('departement/<int:pk>/', DepartementDetailView.as_view(), name='departement-details'),

]
