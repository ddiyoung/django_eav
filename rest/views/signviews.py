# Create your views here.
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest.serializer.signserializer import UserSerializer, SignInSerializer


class SignInView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            raise AuthenticationFailed("아이디와 비밀번호를 확인해주세요.")

        login(request, user)

        return Response()


class SignUpView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
