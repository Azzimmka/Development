from django.contrib import admin
from django.utils.text import slugify
from .models import News, License
from parler.admin import TranslatableAdmin

admin.site.register(License)
@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    exclude = ('created',)  # Исключаем поле 'created' из формы

    def save_model(self, request, obj, form, change):
        # Генерируем slug на основе title, если он не установлен
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)
