from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import book
from .serializers import book_serializer
from django.db.models import Q
# Create your views here.
class booksapi(APIView):
    def post(self,request ,format = None):
        serialized = book_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Data saved successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self, request,format=None):
            search = request.GET.get('search')
            books = book.objects.all()
            if search:
                books = books.filter(Q(title__icontains=search)|Q(author__icontains=search))
            serialized = book_serializer(books,many=True)
            return Response(serialized.data,status=status.HTTP_200_OK)            


class book_details(APIView):
    def get(self, request,id,format=None):
        try:
            getbook = book.objects.get(id=id)
        except book.DoesNotExist:
            return Response({'error': 'Book not found'},status=status.HTTP_404_NOT_FOUND)
        serialized = book_serializer(getbook)
        return Response(serialized.data,status=status.HTTP_200_OK)

    def put(self, request,id,format=None):
        try:
            getbook = book.objects.get(id=id)
        except book.DoesNotExist:
            return Response({'error': 'Book not found'},status=status.HTTP_404_NOT_FOUND)
        serialized = book_serializer(getbook, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Data updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,id,format=None):
        try:
            getbook = book.objects.get(id=id)
        except book.DoesNotExist:
            return Response({'error': 'Book not found'},status=status.HTTP_404_NOT_FOUND)
        serialized = book_serializer(getbook, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Data updated successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,id,format=None):
        try:
            getbook = book.objects.get(id=id)
        except book.DoesNotExist:
            return Response({'error': 'Book not found'},status=status.HTTP_404_NOT_FOUND)
        getbook.delete()
        return Response({'msg': 'Data Deleted Successfully...'},status=status.HTTP_200_OK)
        
        


