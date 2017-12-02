from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def index(request):
    if request.path.strip('/').startswith('api/'):
        raise Http404
    return render(request, 'index.html')
