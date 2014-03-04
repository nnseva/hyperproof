from django.contrib import admin

# Register your models here.

import models

class HyperlinkInline(admin.TabularInline):
    model = models.Hyperlink

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        HyperlinkInline,
    ]

admin.site.register(models.Article,ArticleAdmin)
