from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
# Register your models here.


admin.site.register(News, TranslatableAdmin)
admin.site.register(License)