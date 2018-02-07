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
    wipe_all_data()
    tc_1()

    num_books = Book.objects.all().count()
    num_instances = User.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'books_count': Book.objects.all().count(),
                 'users_count': User.objects.all().count(),
                 'checkouts_count': Checkout.objects.all().count()},
    )


def tc_1():
    log_tc('1')

    book = Book(title="a_book", copies_count=2)
    book.save()

    log_stats('created book')

    patron = Patron.objects.create_user(username='patron', email='patron@lib.co', password='abc')
    patron.save()

    librarian = Librarian.objects.create(username='librarian', email='librarian@lib.co', password='1234567a', libraryCard='123')
    librarian.save()

    do_checkout(patron, book)


def log_stats(action):
    print(action)
    print('books_count: ' + str(Book.objects.all().count()))
    print('users_count: ' + str(User.objects.all().count()))
    print('checkouts_count: ' + str(Checkout.objects.all().count()))


def log_tc(name):
    print('------------- test case ' + name + ' started ------------')


def wipe_all_data():
    call_command('flush', verbosity=0, interactive=False)


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
    if document.copies_count > 1:
        try:
            Checkout.objects.get(user=user, document=document)
            print("You can't checkout")
        except Checkout.DoesNotExist:
            document.copies_count = document.copies_count - 1
            document.save()
            new_checkout = Checkout(user=user, document=document)
            new_checkout.save()
    else:
        print("Check out is not possible. There no available copies")