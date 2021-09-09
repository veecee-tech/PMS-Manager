from outlet.views import OutletAPIView, OutletDetailAPIView
from django.urls import path

urlpatterns = [
    path('', OutletAPIView.as_view(), name="outlet-create"),
    path('detail/<int:id>/', OutletDetailAPIView.as_view(), name='outlet-detail')

]
