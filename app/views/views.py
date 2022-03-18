from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from app.models import Book, Author

from app.serializers import authorSerializer, bookSerializer

# Create your views here.
class retrieveBooks(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        book_list = Book.objects.all()
        serializer = bookSerializer(book_list,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class retrieveAuthors(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        author_list = Author.objects.filter(status=True)
        serializer = authorSerializer(author_list,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class createAuthor(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        data = request.data
        serializer = authorSerializer(data=data)
        # *valida que los valores cumplan con lo que se pide
        serializer.is_valid(raise_exception=True)
        # otra forma
        # if serializer.is_valid():
        #   return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class createBook(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        serializer = bookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


# *Obtener un sólo objeto
class retrieveAuthor(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,author_id):
        author_obj = get_object_or_404(Author,id=author_id)
        serializer = authorSerializer(author_obj)
        return Response(serializer.data)

    def put(self,request,author_id):
        author_obj = get_object_or_404(Author,id=author_id)
        serializer = authorSerializer(instance=author_obj,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,author_id):
        author_obj = get_object_or_404(Author,id=author_id)
        author_obj.status = False
        author_obj.save()
        return Response({'message':'Eliminado'},status=status.HTTP_204_NO_CONTENT)
        


class retrieveBook(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        serializer = bookSerializer(book_obj)
        return Response(serializer.data)