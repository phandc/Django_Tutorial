from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic

from .models import Post
from .serializers import PostSerializer

#third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics
from rest_framework import mixins
#mixins is class that help we reduce time to write repeated code

#Resources in Flask
#compare to Flask Resful
#json payload: payload is the data that being sent or received.

#Create token for admin:  python manage.py drf_create_token admin

#Serialization is the process of converting an object into a stream of bytes to store the object and transmit it to memory, a database, or a file.
#The reverse process is called deserialization

class PostView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)

# class TestView(APIView):

#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         print(request)
#         qs = Post.objects.all()
#         post = qs.first()
#         #serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         print(request)
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)



# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }
#     return JsonResponse(data)


