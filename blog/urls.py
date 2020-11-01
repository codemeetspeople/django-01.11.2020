from django.urls import path
from blog import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('articles/<int:article_id>/', views.ArticleView.as_view())
]
