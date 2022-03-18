from rest_framework import serializers

from app.models import Author, Book

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # *fields = '__all__' para traer todos los datos
        fields = ('id','first_name','last_name','birth_date')


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # *Para traer los datos de la foreign key
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['author'] = authorSerializer(instance.author).data
        return response