from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crear un router para registrar las vistas
router = DefaultRouter()

# Registrar las vistas en el router
router.register(r'moves', views.MovesViewSet, basename='moves')
router.register(r'pokemons', views.PokemonsViewSet, basename='pokemons')
#router.register(r'pokemonsDesc', views.PokemonsDescViewSet, basename='pokemonsDesc')
router.register(r'pokemonsAct', views.PokemonsActViewSet, basename='pokemonsAct')

# Incluir las URLs del router en el archivo de rutas de la app miAPI
urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
]