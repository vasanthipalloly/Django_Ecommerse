from django.contrib import admin
from .models import products,order,profile
# Register your models here.

admin.site.site_header = "E-Commers Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"
#to disply all details in admin pannel
class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default Category'# change df name
    list_display = ('title','price','discount','category','des')
    search_fields = ('title','category','dec',) #tuple
    actions = ('change_category_to_default',)
    #fields = ('title','price',)# to disply required items only ,if we remove this by default admin display all fields
    list_editable = ('price','category',)

admin.site.register(products,ProductAdmin)
admin.site.register(order)
admin.site.register(profile)