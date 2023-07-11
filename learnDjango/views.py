from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    id = random.randint(1, 4)
    article_obj = Article.objects.get(id=id)
    query_set = Article.objects.all()
    # my_list = [123, 78, 90, 987, 908, 45]    
    context = {
        "queryset": query_set,
        "objects": article_obj,
        # "my_list": my_list,
    }
    html_string = render_to_string("home-view.html", context)
    # name = "Dhanveer"
    # if article_obj.id == 1:
    #     h1_string = "<h1>This is empty in the database but if condition is used to render this text</h1>"
    #     p_string = "<p>same goes for paragraph.</p>"
    # else:
    #     h1_string = f'''<h1>title: {article_obj.title}</h1>'''
    #     p_string = f'''<p>content: {article_obj.content}</p>'''

    return HttpResponse(html_string)