from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.customs import MyTokenObtainPairView, CurrentUserView

from .views.departement import (DepartementListView,
                                DepartementCreateView,
                                DepartementDetailView,
                                DepartementUpdateView,
                                DepartementDeleteView)

from .views.service import (ServiceDetailView,
                            ServiceUpdateView,
                            ServiceDeleteView,
                            ServiceListView,
                            ServiceCreateView)

from .views.unit import (UniteListView,
                         UniteCreateView,
                         UniteDetailView,
                         UniteUpdateView,
                         UniteDeleteView)

from .views.user import (UserListView,
                         UserDetailView,
                         UserUpdateView,
                         UserDeleteView,
                         UserCreateView)

app_name = 'authentication'

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token-obtain-pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token-refresh'),
    path('current-user/', CurrentUserView.as_view(), name="current-user"),

    path('user/', UserListView.as_view(), name='user-list'),
    path('user/create', UserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    path('service/', ServiceListView.as_view(), name='service-list'),
    path('service/create', ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),

    path('unite/', UniteListView.as_view(), name='unite-list'),
    path('unite/create', UniteCreateView.as_view(), name='unite-create'),
    path('unite/<int:pk>/', UniteDetailView.as_view(), name='unite-detail'),
    path('unite/<int:pk>/update/', UniteUpdateView.as_view(), name='unite-update'),
    path('unite/<int:pk>/delete/', UniteDeleteView.as_view(), name='unite-delete'),

    path('departement/', DepartementListView.as_view(), name='departement-list'),
    path('departement/create', DepartementCreateView.as_view(), name='departement-create'),
    path('departement/<int:pk>/', DepartementDetailView.as_view(), name='departement-detail'),
    path('departement/<int:pk>/update/', DepartementUpdateView.as_view(), name='departement-update'),
    path('departement/<int:pk>/delete/', DepartementDeleteView.as_view(), name='departement-delete'),

]
