from django.contrib import admin
from .models import Products,productCertificate,productReview,Store

class productReviewInline(admin.TabularInline):
    model=productReview
    extra=2

class productsAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[productReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('products',)

class ProductCertificateAdmin(admin.ModelAdmin):
    list_display=('product','certificate_number')


# Register your models here.
admin.site.register(Products,productsAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(productCertificate,ProductCertificateAdmin)