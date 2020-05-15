from django.contrib.postgres.search import SearchVector
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from consoles.forms.forms import SearchForm
from consoles.models import Console


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles = [{
            'id': x.id,
            'name': x.console_name,
            'description': x.console_short_description,
            'firstImage': x.consoleimage_set.first().console_image_image
        } for x in Console.objects.filter(console_name__icontains=search_filter)]

        return JsonResponse({'data': consoles})

    consoles = Console.objects.all().order_by('console_name')
    paginator = Paginator(consoles, 6)
    page = request.GET.get('page')
    paged_consoles = paginator.get_page(page)
    context = {'console': paged_consoles}

    return render(request, 'consoles/index.html', context=context)


def get_console_by_id(request, id):
    return render(request, 'consoles/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })


def console(request, id):
    console = get_object_or_404(Console, pk=id)
    context = {'console': console}
    return render(request, 'consoles/console_details.html', context=context)


def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Console.objects.annotate(
                search=SearchVector('console_name', 'console_short_description', 'console_long_description'),
            ).filter(search=query)
    context = {
        'form': form,
        'query': query,
        'results': results,
    }
    return render(request, 'consoles/search.html', context)
