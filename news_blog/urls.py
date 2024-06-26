from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),   
    path('<int:article_id>/', views.get_article, name='article'), 
    path("/about", views.about, name='about'),   
]

