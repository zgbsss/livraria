from rest_framework.serializers import ModelSerializer

from livraria.models import Autor, Categoria, Editora

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"