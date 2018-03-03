from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('/list/', views.base_list, name='base-list'),
    url('books/', views.BookListView.as_view(), name='books'),
    url('book/<int:pk>', views.book_detail_view, name='book-detail'),
]