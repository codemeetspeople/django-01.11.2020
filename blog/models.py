from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    title = models.CharField(
        null=False,
        max_length=100,
        verbose_name=_('Название')
    )

    def __str__(self):
        return self.title


class Article(models.Model):
    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    title = models.CharField(
        null=False,
        max_length=100,
        verbose_name=_('Название')
    )
    content = models.TextField(
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        to='Category',
        related_name='articles',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        to=USER_MODEL,
        related_name='articles',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} ({self.category.title})'
