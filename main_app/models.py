from django.db import models


rate_table = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
}


class Category(models.Model):  # Категория новости
    name = models.CharField(max_length=255, unique=True, blank=False, null=True, verbose_name='News` categories')

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.IntegerField(blank=False, null=True, choices=rate_table, verbose_name='User rate')

    def __str__(self):
        return str(self.rate)


class News(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Title')
    desc = models.TextField(blank=False, null=False, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False, null=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name='news', verbose_name='Category')
    rate = models.ManyToManyField(Rate, blank=True, null=True)
    avg_rate = models.FloatField(blank=True, null=True, verbose_name='Average rate')

    def __str__(self):
        return self.title

