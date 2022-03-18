from django.urls import path

from app.views import views, modelview


urlpatterns = [
    path('books', views.retrieveBooks.as_view()),
    path('books/create', views.createBook.as_view()),
    path('books/<int:book_id>', views.retrieveBook.as_view()),
   
    path('authors', views.retrieveAuthors.as_view()),
    path('authors/create', views.createAuthor.as_view()),
    path('authors/<int:author_id>', views.retrieveAuthor.as_view()),

    path('viewset/authors', modelview.authorViewSet.as_view({'get':'list'})),
    path('viewset/authors/create', modelview.authorViewSet.as_view({'post':'create'})),
    path('viewset/authors/<int:author_id>', modelview.authorViewSet.as_view({'get':'retrieve','put':'partial_update','delete':'destroy'})),
]