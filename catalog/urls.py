from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('books/', views.BookListView.as_view(), name='books'),
    path('books2/', views.BookListView.as_view(), name='books2'),

    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

]



#pointing to LoanedBooksByUserListView (define in views )
urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]



#pointing to LoanedBooksByLibrarianListView (define in views )
urlpatterns += [   
    path('allborrowed/', views.LoanedBooksByLibrarianListView.as_view(), name='all-borrowed'),
]



urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]




urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]




urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]




urlpatterns += [  
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]















