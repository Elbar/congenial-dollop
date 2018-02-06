from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Book, Checkout
from account.models import Librarian

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = Checkout.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances},
    )


class BookListView(generic.ListView):
    model = Book


def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
        checkout = Checkout.objects.get(document=book_id)
        is_librarian = isinstance(request.user, Librarian)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    return render(
        request,
        'catalog/book_detail.html',
        context={'book': book_id, 'checkout':checkout, 'is_librarian': is_librarian}
    )


