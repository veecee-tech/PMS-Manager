from django.urls import path


from .views import RangeAPIView, RangeDetailAPIView, CategoryAPIView, CategoryDetailAPIView


urlpatterns = [
    path('category/',CategoryAPIView.as_view(), name='category'),
    path('category/<int:id>/', CategoryDetailAPIView.as_view(), name='category-list'),
    
    path('',RangeAPIView.as_view(), name='range'),
    path('<int:id>/', RangeDetailAPIView.as_view(), name='range-list'),
]