from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import CategoryAPIViewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rangeCategory.models import Category
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# class CategoryAPIView(ListCreateAPIView):

#     serializer_class = CategoryAPIViewSerializer
#     queryset = Category.objects.all()
#     permission_classes=(permissions.IsAuthenticated, IsOwner)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

#     def queryset(self,request):
#         return Category.objects.filter(owner=request.user)
    
# class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    
#     serializer_class = CategoryAPIViewSerializer
#     queryset = Category.objects.all()
#     permission_classes=(permissions.IsAuthenticated,IsOwner)
#     lookup_field = "id"
   

#     def queryset(self):
#         return Category.objects.all()



@api_view(['GET', 'POST'])
def post_list(request, *args, **kwargs):
    permission_classes=(permissions.IsAuthenticated, IsOwner)

    if request.method == 'GET':
        posts = Category.objects.filter(user=request.user)
        serializer = CategoryAPIViewSerializer(posts, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategoryAPIViewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, *args, **kwargs):
    permission_classes=(permissions.IsAuthenticated, IsOwner)
    try:
        pk = int(kwargs['pk'])
        post = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoryAPIViewSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoryAPIViewSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
