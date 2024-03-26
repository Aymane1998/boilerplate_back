from authentication import views

from django.urls import path

from rest_framework_simplejwt import views as jwt_views


from .views.customs import CurrentUserView, MyTokenObtainPairView
from .views.departement import (
    DepartementCreateView,
    DepartementDeleteView,
    DepartementDetailView,
    DepartementListView,
    DepartementUpdateView,
)
from .views.service import (
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailView,
    ServiceListView,
    ServiceUpdateView,
)
from .views.unit import (
    UniteCreateView,
    UniteDeleteView,
    UniteDetailView,
    UniteListView,
    UniteUpdateView,
)
from .views.user import (
    ConfirmationActivationUserView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
)


app_name = "authentication"

urlpatterns = [
    path("api/token/", MyTokenObtainPairView.as_view(), name="token-obtain-pair"),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"
    ),
    path(
        "api/forgotten-password/",
        views.ForgottenPasswordView.as_view(),
        name="forgotten-password",
    ),
    path(
        "api/reset-password/", views.ResetPasswordView.as_view(), name="reset-password"
    ),
    path("current-user/", CurrentUserView.as_view(), name="current-user"),
    path("user/", UserListView.as_view(), name="user-list"),
    path("user/create-user/", UserCreateView.as_view(), name="user-create"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path(
        "user/confirmation-activation-user/<str:token>/",
        ConfirmationActivationUserView.as_view(),
        name="confirmation-activation-user",
    ),
    path("service/", ServiceListView.as_view(), name="service-list"),
    path("service/create", ServiceCreateView.as_view(), name="service-create"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
    path(
        "service/<int:pk>/update/", ServiceUpdateView.as_view(), name="service-update"
    ),
    path(
        "service/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service-delete"
    ),
    path("unite/", UniteListView.as_view(), name="unite-list"),
    path("unite/create", UniteCreateView.as_view(), name="unite-create"),
    path("unite/<int:pk>/", UniteDetailView.as_view(), name="unite-detail"),
    path("unite/<int:pk>/update/", UniteUpdateView.as_view(), name="unite-update"),
    path("unite/<int:pk>/delete/", UniteDeleteView.as_view(), name="unite-delete"),
    path("departments/", DepartementListView.as_view(), name="departement-list"),
    path(
        "department/create", DepartementCreateView.as_view(), name="departement-create"
    ),
    path(
        "department/<int:pk>/",
        DepartementDetailView.as_view(),
        name="departement-detail",
    ),
    path(
        "department/<int:pk>/update/",
        DepartementUpdateView.as_view(),
        name="departement-update",
    ),
    path(
        "department/<int:pk>/delete/",
        DepartementDeleteView.as_view(),
        name="departement-delete",
    ),
]
