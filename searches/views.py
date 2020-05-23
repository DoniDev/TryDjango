from django.shortcuts import render
from . models import SearchQuery
from blog.models import BlogPost

def search(request):
    query = request.GET.get('q', None)
    context = {'query': query}
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(query=query,user=user)
        results = BlogPost.objects.all().search(query=query)
        context['results'] = results
    return render(request, 'search/view.html', context=context)
