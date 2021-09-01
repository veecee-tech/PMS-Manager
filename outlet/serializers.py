from outlet.models import Outlet
from rest_framework import serializers


class OutletAPIViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outlet
        fields = "__all__"

