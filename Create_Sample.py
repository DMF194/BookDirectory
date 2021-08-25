>>> author = Author(name='Lisa Unger',age=45)
>>> author.save()
>>> genre = Genre(name='Thriller')
>>> genre.save()
>>> genre = Genre(name='Fiction')
>>> genre.save()


>>> book = Book(name='Learn ABC', price=200, author=author)
>>> book.genre.add(Genre.objects.get('Thriller'))
>>> book.save()