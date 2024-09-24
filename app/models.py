from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.

from django.utils.text import slugify

class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=200),
        description=models.CharField(_('description'), max_length=5200)
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL') 
    logo = models.ImageField(upload_to='asia_logos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('New')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Person(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('name'), max_length=1500),
        department = models.CharField(_('department'), max_length=1500),
        share_capital = models.CharField(_('share_capital'), max_length=1500),
        share_fund = models.CharField(_('share_fund'), max_length=1500),
    )

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return self.name
    
class Tenders(TranslatableModel):
    translations = TranslatedFields(
        title =  models.CharField(_('title'), max_length=1000),
        description = models.TextField(_('description')),
    )
    pdf = models.FileField(upload_to='tenders/', null=True, blank=True) 
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('Tender')
        verbose_name_plural = _('Tenders')
    
    def __str__(self):
        return f"{self.title} | {self.start_time}"

class License(models.Model):
    name = models.CharField(max_length=255)  # Имя лицензии
    pdf = models.FileField(upload_to='licenses/', null=True, blank=True) 

    class Meta:
        verbose_name = _('License')
        verbose_name_plural = _('Licenses')

    def __str__(self):
        return self.name




class Year(models.Model):
    year = models.PositiveIntegerField(verbose_name="Год") 
    
    class Meta:
        verbose_name = _('Year')
        verbose_name_plural = _('Years')

    def __str__(self):
        return str(self.year)


class FinancialData(TranslatableModel):
    translations = TranslatedFields(
        indicator_name = models.CharField(max_length=255, verbose_name=_("Показатель")),
        unit = models.CharField(max_length=50, verbose_name=_("Ед. изм."))
    )

    values = models.ManyToManyField(Year, through='FinancialYearData', )

    class Meta:
        verbose_name = _('FinancialData')
        verbose_name_plural = _('FinancialData')

    def __str__(self):
        return self.safe_translation_getter('indicator_name', any_language=True)


class FinancialYearData(models.Model):
    financial_data = models.ForeignKey(FinancialData, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    value = models.CharField(max_length=200 , verbose_name="Значение", blank=True, null=True)

    class Meta:
        verbose_name = _('FinancialYearData')
        verbose_name_plural = _('FinancialYearData')

    def __str__(self):
        return f'{self.financial_data.safe_translation_getter("indicator_name", any_language=True)} - {self.year.year}'


class Management(TranslatableModel):
    translations = TranslatedFields(
        f_i_o = models.CharField(_('F_I_O'), max_length=1500),
        position = models.CharField(_('position'), max_length=1500),
        еducation = models.CharField(_('еducation'), max_length=1400),
        specialization = models.CharField(_('specialization'), max_length=1500),
        phone = models.CharField(_('phone'), max_length=1500),
        admission_date = models.CharField(_('admission_date'), max_length=1300),
        admission_time = models.CharField(_('admission_time'),max_length=1300 ),
    )
    img = models.ImageField(upload_to='management/', null=True, blank=True)

    class Meta:
        verbose_name = _('Management')
        verbose_name_plural = _('Managements')

    def __str__(self):
        return self.safe_translation_getter('f_i_o', any_language=True)


class MoreInfo(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=1500),
    )
    pdf = models.FileField(upload_to='more_info/', null=True, blank=True)
    pdf2 = models.FileField(upload_to='more_info/', null=True, blank=True)

    class Meta:
        verbose_name = _('MoreInfo')
        verbose_name_plural = _('MoreInfos')

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
    

class Vacancy(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=1500),
        description = models.CharField(_('description'), max_length=1500),
    )
    phone = models.CharField(_('phone'), max_length=1500)

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)