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


#create a article
def article_create_view(request):

    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        #print(title, content)
        article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    #context = {}
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):

    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
