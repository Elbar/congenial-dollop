from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Book, Checkout, Document
from .forms import DocumentForm
from django.shortcuts import redirect
from account.models import User, Patron, Librarian


class BookListView(generic.ListView):
    model = Book


def base_list(request):
    return render(request,
                  'catalog/base_list.html',
                  context={})


def index(request):
    """
    View function for home page of site.
    """
    return render(
        request,
        'catalog/base_list.html',
        context={},
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
        'catalog/base_detail.html',
        context={'book': book_id, 'checkout': checkout, 'is_librarian': is_librarian}
    )


def create_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = DocumentForm()
    return render(request, 'catalog/document_edit.html', {'form': form})