from http.client import HTTPResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .forms import BookCreateForm, BookEditForm
from .models import Books

@require_http_methods(['GET'])
def book_list(request):
    book_list = Books.objects.all()
    form = BookCreateForm(auto_id=False)

    return render(request, 'base.html', {
        'book_list': book_list,
        'form': form,
    })

@require_http_methods(['POST'])
def book_create(request):
    form = BookCreateForm(request.POST)
    if form.is_valid():
        book = form.save()
    return render(request, 'partial_book_detail.html', {'book': book})

def update_book_details(request, pk):
    book = get_object_or_404(Books, pk=pk)

    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return render(request, 'partial_book_detail.html', {'book':book})

    else:
        BookEditForm(instance=book)
    return render(request, 'partial_book_update_form.html', {
        'book':book,
        'form': form,
    })

@require_http_methods(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    return render(request, 'partial_book_detail.html', {'book': book})

@require_http_methods(["DELETE"])
def book_delete(request, pk):
    book = get_object_or_404(Books, pk)
    book.delete()
    return HTTPResponse()

@require_http_methods(['PATCH'])
def book_status_change(request, pk):
    book = get_object_or_404(Books, pk)
    book.read = not book.read
    return render(request, 'partial_book_detail.html', {'book':book})
