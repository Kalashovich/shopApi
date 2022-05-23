from curses.textpad import rectangle

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from account.send_email import send_confirmation_email, send_reset_password 
from . import serializers
# from account import serializers

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView


User = get_user_model()


class RegistrationApiView(APIView):
    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg':'Successfully activated!'},status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(TokenObtainPairView):
    serializers_class = serializers.LoginSerializer


# class LogoutApiView(LogoutView):
#     permissions_classes = (permissions, IsAuthenticated)

class NewPasswordView(APIView):
    def post(self, request):
        serializer = serializers.CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('password chan')


class ResetPasswordView(APIView):

    def post(self, request):
        serializer = serializers.PasswordResetSerizlizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(email=serializer.data.get('email'))
            user.create_activation_code()
            user.save()
            send_reset_password(user)
            return Response('check your email')
            

class LogoutAPIView(GenericAPIView):
    serializer_class = serializers.LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out!', status=status.HTTP_204_NO_CONTENT)
