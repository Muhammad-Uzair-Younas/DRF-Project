from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    # List and Create operations share the same base path
    path('books/', views.booksapi.as_view(), name='books_list'),    
    # Detail, Update, and Delete operations require the ID parameter
    path('books/<int:id>/', views.book_details.as_view(), name='book_details'),
]
