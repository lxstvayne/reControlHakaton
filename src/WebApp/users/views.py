from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import generics

from . import serializers, models


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.RegisterSerializer


class RetrieveUpdateProfileView(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfessionListView(generics.ListAPIView):
    serializer_class = serializers.UserProfession
    queryset = models.Profession.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
