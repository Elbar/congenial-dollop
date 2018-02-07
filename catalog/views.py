from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Book, Checkout, Document
from account.models import User, Patron, Librarian


def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'books_count': Book.objects.all.count, 'checkouts_count': Checkout.objects.all.count},
    )


class BookListView(generic.ListView):
    model = Book


def wipe_all_data():
    Document.objects.all.delete
    User.objects.all.delete
    Checkout.objects.all.delete


def print_counts():
    print('books_count: ' + Book.objects.all.count + ' | checkouts_count: ' + Checkout.objects.all.count)


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


def do_checkout(user, document):
    if document.numberOfCopies > 1:
        try:
            Checkout.objects.get(user=user, document=document)
            print("You can't checkout")
        except Checkout.DoesNotExist:
            document.numberOfCopies = document.numberOfCopies - 1
            document.save
            new_checkout = Checkout(user=user, document=document)
            new_checkout.save
    else:
        print("Check out is not possible. There no available copies")