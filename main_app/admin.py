from django.contrib import admin
from .models import News, Category


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category')


admin.site.register(News)
# admin.site.register(NewsAdmin)
admin.site.register(Category)

