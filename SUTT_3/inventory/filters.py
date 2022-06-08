import django_filters
from .models import inventory

class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = inventory
        fields = '__all__'
