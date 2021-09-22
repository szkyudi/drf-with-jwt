from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    InvalidToken
)


class TokenObtainAndSetCookieView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )
        response.set_cookie(
            key='refresh',
            value=serializer.validated_data['refresh'],
            httponly=True,
            max_age= 60 * 60 * 24 * 60
        )
        return response


class TokenRefreshAndSetCookieView(TokenRefreshView):
    def get(self, request, *args, **kwargs):
        data = {"refresh": request.COOKIES['refresh']}
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )
        response.set_cookie(
            key='refresh',
            value=serializer.validated_data['refresh'],
            httponly=True,
            max_age= 60 * 60 * 24 * 60
        )
        return response
