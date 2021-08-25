from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE, ManyToManyField

# Model for Author, Fields - Name, age
class Author(models.Model):
    name = CharField(max_length=100)
    age = IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

# Model for Genre, Fields - Name
class Genre(models.Model):
    name = CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

# Model for Book, Field - name, price, author(link back to Model for Author), genres(link back to Model for Genre)
class Book(models.Model):
    id_book = IntegerField()
    name = CharField(max_length=100)
    price = IntegerField()
    author = ForeignKey(Author, on_delete=CASCADE, related_name='books')
    genres = ManyToManyField(Genre, related_name='books')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'name: {self.name}, price: {self.price}'