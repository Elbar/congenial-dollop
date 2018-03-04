from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.shortcuts import redirect
from account.models import *


def index(request):
    """
    View function for home page of site.
    """

    return render(
        request,
        'index.html',
        context={'documents_count': Document.objects.count(), 'users_count': User.objects.count(),
                 'checkouts_count': Checkout.objects.count()},
    )


def books(request):
    queryset = request.user.get_queryset()
    return render(request,
                  'catalog/book_list.html',
                  context={'books': Book.objects.all(), 'queryset': queryset})


def documents(request):
    queryset = request.user.get_queryset()

    return render(request, 'catalog/document_list.html',
                  context={'documents': Document.objects.all(),'queryset': queryset})


def articles(request):
    return render(request,
                  'catalog/article_list.html',
                  context={'documents': JournalArticle.objects.all()})


def users(request):
    return render(request,
                  'catalog/user_list.html',
                  context={'users': User.objects.all()})


def checkouts(request):
    queryset = request.user.get_queryset()
    return render(request, 'catalog/checkout_list.html', context={'checkouts': Checkout.objects.all(), 'queryset':queryset})


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
            redirect('catalog/document_edit.html')
    else:
        form = DocumentForm()
    return render(request, 'catalog/document_edit.html', {'form': form})


def create_checkout(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = CheckoutForm()
    return render(request, 'catalog/document_edit.html', {'form': form})


def do_checkout(request, document_id):
    current_user = request.user
    document = Document.objects.get(id=document_id)
    if document.get_copies_count() > 0:
        if Checkout.objects.filter(document=document, user=current_user).exists() is False:
            new_checkout = Checkout(document=document, user=current_user)
            new_checkout.save()
            return render(request, 'catalog/base_detail.html',
                          context={'document': document, 'is_checked': True})

    return render(request, 'catalog/base_detail.html', context={'document': document, 'is_checked': False})

