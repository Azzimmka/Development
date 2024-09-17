from django.db import models
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
        # Генерация slug, если он не задан
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    

class License(models.Model):
    name = models.CharField(max_length=255)  # Имя лицензии
    pdf = models.FileField(upload_to='licenses/', null=True, blank=True) 

    def __str__(self):
        return self.name


