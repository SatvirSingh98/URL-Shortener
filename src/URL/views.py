from django.shortcuts import get_object_or_404, redirect, render
from .models import UrlShortener


def shortener(request):
    if request.method == 'POST':
        full_url = request.POST.get('full_url')
        obj, _ = UrlShortener.objects.get_or_create(original_url=full_url)
        print(obj)
        context = {'full_url': full_url, 
                   'short_url': f'{request.get_host()}/{obj.slug}'}
        return render(request, 'URL/index.html', context)
    return render(request, 'URL/index.html')



def redirect_url(request, slug):
    obj = get_object_or_404(UrlShortener, slug=slug)
    return redirect(obj.original_url)
