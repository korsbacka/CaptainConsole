from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from games.models import Game


def index(request):
    games = Game.objects.all().order_by('game_name')

    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)
    context = {'games': paged_games}

    return render(request, 'games/index.html', context=context)


def get_game_by_id(request, id):
    return render(request, 'games/game_details.html', {
        'game': get_object_or_404(Game, pk=id)
    })


def game(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {'game': game}
    return render(request, 'games/game_details.html', context=context)