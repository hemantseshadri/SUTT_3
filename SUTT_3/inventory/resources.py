from import_export import resources
from .models import inventory

class inventoryResource(resources.ModelResource):
    class Meta:
        model=inventory
