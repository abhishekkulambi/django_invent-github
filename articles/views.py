from django.shortcuts import render

from .models import Article
# Create your views here.

#search_view
def article_search_view(request):
    query_dict = request.GET    #this is a dict
    #query = query_dict.get('q')  #<input type="text" name='q'/>
    #print(request.GET)
    try:
        query = int(query_dict.get("q")) 
    except:
        query = None

    article_obj = None 
    if query is not None:
        article_obj = Article.objects.get(id=query)   #basic search type

    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):

    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
