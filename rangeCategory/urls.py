from django.urls import path
from .views import post_list, post_detail
# from .views import CategoryDetailAPIView, CategoryAPIView
# from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('',post_list),
    path('<int:pk>/',post_detail),

    # path('',CategoryAPIView.as_view(), name='category'),
    # path('<int:id>/', CategoryDetailAPIView.as_view(), name='category-list'),
]