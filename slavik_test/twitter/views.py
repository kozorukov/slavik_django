from django.shortcuts import render
from django.http import HttpRequest

from twitter.forms import TwittersForm
from twitter.twitter_service.main import get_twitters_information


def twitter(request: HttpRequest):
    if request.method == 'POST':
        form = TwittersForm(request.POST)
        information = get_twitters_information(request.POST.get('text'))
    else:
        form = TwittersForm()
        information = ''

    data = {
        'form': form,
        'information': information
    }

    return render(request, 'twitter.html', data)
