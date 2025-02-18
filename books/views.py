from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import BookCreateForm
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
    return render(request, 'partial_book_list.html', {'book': book})
