from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe

from .models import Blog, Category


# Register your models here.
admin.site.register(Category)


class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    small_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Blog
        fields = '__all__'



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'trending')
    list_filter = ('category', 'date')
    search_fields = ('title', 'category__name')
    save_on_top = True
    save_as = True
    list_editable = ('trending',)
    form = BlogAdminForm
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('title', 'small_description'),)
        }),
        (None, {
            'fields': ('description', ('image', 'get_image'))
        }),
        (None, {
            'fields': (('category', 'tags', 'type'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={f"http://127.0.0.1:8000{obj.image.url}"} width="100" height="60">')

    get_image.short_description = 'Image'



