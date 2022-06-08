from django.contrib import admin
from .models import inventory,IssueItem, Userlog, IsMod, Category, Moderatorlog
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(inventory)

class inventoryAdmin(ImportExportModelAdmin):
    list_display=('Item_name','Quantity','category')
admin.site.register(IssueItem)
admin.site.register(Category)
admin.site.register(Userlog)
admin.site.register(IsMod)
admin.site.register(Moderatorlog)
