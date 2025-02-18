from django.db import models


class Books(models.Model):
    """ Модель книги """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    read = models.BooleanField(verbose_name="Readed", default=False)

    def __str__(self):
        return self.title


