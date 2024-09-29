from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Title')
    desc = models.TextField(blank=False, null=False, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)

