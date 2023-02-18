from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/register/', views.CreateUserView.as_view()),
    path('api/profile', views.RetrieveUpdateProfileView.as_view()),
    path('api/professions', views.ProfessionListView.as_view()),
]
