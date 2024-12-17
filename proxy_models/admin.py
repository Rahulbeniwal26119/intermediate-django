from django.contrib import admin
from proxy_models.models import Product, ArchivedProducts, ProductLegacyProxy


class BaseProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'is_deleted']
    search_fields = ['name']
    list_filter = ['is_deleted']


admin.site.register(Product, BaseProductAdmin)
admin.site.register(ArchivedProducts, BaseProductAdmin)
admin.site.register(ProductLegacyProxy, BaseProductAdmin)