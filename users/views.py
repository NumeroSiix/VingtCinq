from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(email=self.request.user.email)

    def perform_update(self, serializer):
        if serializer.instance.email != self.request.user.email:
            raise PermissionDenied('You do not have permission to perform this action.')
        serializer.save()

    def perform_destroy(self, instance):
        if instance.email != self.request.user.email:
            raise PermissionDenied('You do not have permission to perform this action.')
        instance.delete()
