from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Outlet
from .permissions import IsOwner
from .serializers import OutletAPIViewSerializer


# Create your views here.

class OutletAPIView(ListCreateAPIView):
    serializer_class = OutletAPIViewSerializer
    queryset = Outlet.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Outlet.objects.filter(user=self.request.user)


class OutletDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OutletAPIViewSerializer
    queryset = Outlet.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"

    def get_queryset(self):
        return Outlet.objects.all()
