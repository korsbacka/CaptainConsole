from django.shortcuts import render

from consoles.models import Console


def index(request):
    context = {'consoles': Console.objects.all().order_by('console_name')}
    return render(request, 'consoles/index.html', context=context)
