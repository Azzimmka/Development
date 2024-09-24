from django.contrib import admin
from django.utils.text import slugify
from .models import *
from parler.admin import TranslatableAdmin


admin.site.register(License)

@admin.register(Management)
class ManagementAdmin(TranslatableAdmin):
    list_display = ('f_i_o', 'position', 'еducation', 'specialization', 'phone', 'admission_date', 'admission_time')

@admin.register(Person)
class PersonAdmin(TranslatableAdmin):
    list_display = ('name', 'department', 'share_capital', 'share_fund')

@admin.register(Tenders)
class TendersAdmin(TranslatableAdmin):
    list_display = ('title', 'description')


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    exclude = ('created',)  # Исключаем поле 'created' из формы

    def save_model(self, request, obj, form, change):
        # Генерируем slug на основе title, если он не установлен
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)



class FinancialYearDataInline(admin.TabularInline):
    model = FinancialYearData
    extra = 1

class FinancialDataAdmin(TranslatableAdmin):
    inlines = [FinancialYearDataInline]
    list_display = ('indicator_name', 'unit')

admin.site.register(Year)
admin.site.register(FinancialData, FinancialDataAdmin)


@admin.register(MoreInfo)
class MoreInfoAdmin(TranslatableAdmin):
    list_display = ('title',) 

@admin.register(Vacancy)
class VacancyAdmin(TranslatableAdmin):
    list_display = ('title', 'description')
