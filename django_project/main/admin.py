from django.contrib import admin
from .models import Cards, Gallery
from .forms import GalleryForms
# Register your models here.

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    readonly_fields = ('image_tag', 'size')
    form = GalleryForms

@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
    list_display=('__str__', 'decs_return')
    readonly_fields = ('size_warning', )
    search_fields = ('title', 'desc')
    