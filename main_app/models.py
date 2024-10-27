from django.db import models
from ege.models import Category


class News(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Title')
    desc = models.TextField(blank=False, null=False, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL, related_name='news', verbose_name='Category')

