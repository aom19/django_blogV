
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogListSerializer


class BlogList(APIView):
    def get(self,request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs,many=True)
        return Response(serializer.data)


class BlogDetail(APIView):
    def get(self,request,pk):
        blog = Blog.objects.get(id=pk)
        serializer = BlogListSerializer(blog)
        return Response(serializer.data)

