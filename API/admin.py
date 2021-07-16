from django.contrib import admin

from .models import *

from import_export import resources

from import_export.admin import ImportExportModelAdmin

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name','state')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = CategoryResource

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):
    list_display = ('id','name','autor','state','image_book','category','file')
    readonly_fields = ('created', 'updated')
    search_fields = ['name','autor']
    resource_class = BookResource

admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)