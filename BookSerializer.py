class BookSerializer(serializers.ModelSerialzer):
    class Meta:
        model = Book
        fields = ['name', 'price', 'id_book']
