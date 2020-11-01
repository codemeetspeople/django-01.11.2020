from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from blog import models


class IndexView(TemplateView):
    template_name = 'blog/index.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'categories': models.Category.objects.all()
        })

        return context


class ArticleView(TemplateView):
    template_name = 'blog/article.tpl'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article_id = kwargs.get('article_id')
        article = get_object_or_404(models.Article, pk=article_id)

        context.update({
            'article': article
        })

        return context
