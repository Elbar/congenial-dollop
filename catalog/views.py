from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Book, Checkout, Document
from account.models import User, Patron, Librarian
from django.core.management import call_command


class BookListView(generic.ListView):
    model = Book


def index(request):
    """
    View function for home page of site.
    """
    # num_books = Book.objects.all().count()
    # num_instances = User.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'books_count': Book.objects.all().count(),
                 'users_count': User.objects.all().count(),
                 'checkouts_count': Checkout.objects.all().count()},
    )


def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
        checkout = Checkout.objects.get(document=book_id)
        is_librarian = hasattr(request.user, 'librarian')
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(
        request,
        'catalog/book_detail.html',
        context={'book': book_id, 'checkout': checkout, 'is_librarian': is_librarian}
    )

