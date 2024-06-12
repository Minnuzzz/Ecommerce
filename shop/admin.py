from django.contrib import admin
from.models import product,category
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','update']
    list_editable = ['price','stock','available']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,productadmin)