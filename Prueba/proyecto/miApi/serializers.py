from rest_framework import serializers
from .models import Moves, MovesPokemons, Pokemons

class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = ['id', 'name', 'type', 'power', 'accuracy']  

class PokemonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemons
        fields = ['id', 'name']

class PokemonsDescSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()  # Usamos SerializerMethodField para obtener los movimientos
    class Meta:
        model = Pokemons
        fields = ['id', 'name', 'type_1', 'type_2', 'description', 'height', 'weight', 'moves']
    def get_moves(self, obj):
        # Accedemos a los movimientos a través de la tabla intermedia
        moves = Moves.objects.filter(movespokemons__pokemon=obj)
        return MovesSerializer(moves, many=True).data