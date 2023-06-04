from django.contrib import admin
from .models import *


class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Type, TypeAdmin)
admin.site.register(Tour)
admin.site.register(Images)
admin.site.register(TourGallery)
admin.site.register(TourExp)
