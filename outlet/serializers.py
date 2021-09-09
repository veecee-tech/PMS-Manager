from rest_framework import serializers

from outlet.models import Outlet


class OutletAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = "__all__"
