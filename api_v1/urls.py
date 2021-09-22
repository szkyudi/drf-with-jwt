from django.urls import path, include

from user.views import (
    TokenObtainAndSetCookieView,
    TokenRefreshAndSetCookieView
)

app_name = 'api_v1'
urlpatterns = [
    path('auth/jwt/create/', TokenObtainAndSetCookieView.as_view()),
    path('auth/jwt/refresh/', TokenRefreshAndSetCookieView.as_view()),
    path('auth/', include('djoser.urls')),
]
