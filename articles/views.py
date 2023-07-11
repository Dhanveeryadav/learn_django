from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article

from .forms import ArticleForm
# Create your views here.
def article_details(request, id):
    detail_object = Article.objects.get(id=id)
    context = {
        "object": detail_object
    }

    return render(request, "article/details.html", context)

def article_search_view(request):
    # print(dir(request))
    print(request.GET)
    query_dict = request.GET
    # query = query_dict.get("q")
    try:
        query = query_dict.get("q")
    except:
        query = None
    article_object = None
    if query is not None:
        article_object = Article.objects.get(id=query)
    context = {
        "object": article_object
    }    
    return render(request, "article/search-form.html", context=context)

@login_required
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None) 
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context["form"] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # article_object = Article.objects.create(title=title, content=content)
        # context["object"] = article_object
        # context["created"] = True 
    return render(request, "article/create.html", context)