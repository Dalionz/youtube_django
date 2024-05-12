from django.shortcuts import render
from goods.models import Categories


def index(request):

    context = {
        'title': 'HOME - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': ' HOME - О нас',
        'content': 'О нас',
        'text_on_page': 'Наш магазин предлагает широкий ассортимент мебели в различных ценовых категориях. '
    }
    return render(request, 'main/about.html', context)


