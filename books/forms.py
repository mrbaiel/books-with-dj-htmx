from django.forms import Form, ModelForm, CharField, TextInput

from books.models import Books


class BookCreateForm(ModelForm):
    title = CharField(required=False, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Название"}))
    author = CharField(required=False, widget=TextInput(attrs={"class":"clrtxt", "placeholder": "Автор"}))
    price = CharField(required=False, widget=TextInput(attrs={"class":"clrtxt", "placeholder": "Цена"}))


    class Meta:
        model = Books
        fields = ['title', 'author', 'price']