from django.contrib import admin
from servee_document.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Document, DocumentAdmin)
