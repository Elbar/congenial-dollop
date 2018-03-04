from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('/users/', views.users, name='users'),
    url('/checkouts/', views.checkouts, name='checkouts'),
    url('/document/new/', views.create_checkout, name='document_new'),
    url('/documents', views.documents, name='documents'),
    url('/books/', views.books, name='books'),
    url('/articles/', views.articles, name='articles'),
    url('^document/(?P<document_id>\d+)/$',views.do_checkout, name='checkout-detail'),
]