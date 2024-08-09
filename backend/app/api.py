from ninja import NinjaAPI

from .models import Wine


api = NinjaAPI()


@api.get('/list')
def list(request):
    wines = Wine.objects.all()

    return [
        {'id': wine.id, 'name': wine.name, 'year': wine.year,
         'appellation': wine.appellation} for wine in wines
    ]
