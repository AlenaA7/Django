from django.shortcuts import render

# Create your views here.

def get_article(request, article_id):
    article = articles[article_id-1]
    return render(request, 'news_blog/news_article.html', {'article': article})

def index(request):
    return render(request, 'news_blog/news_list.html', {'articles': articles})

def about(request):
    return render(request, 'news_blog/about.html', {'articles': articles})


articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]
