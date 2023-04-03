from django.shortcuts import render

from various.models import Theme


def index(request):
    themes = Theme.objects.all()
    return render(
        request,
        "documentary_watch/index.html",
        {'themes': themes}
    )