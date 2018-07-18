from django.contrib import admin

# Register your models here.
from .models import Inventory, InventoryCountAsof, SupplierPOItems, \
    MaterialRequisition, SupplierPO, SupplierRawMaterials

admin.site.register(SupplierPO)
admin.site.register(SupplierPOItems)
admin.site.register(Inventory)
admin.site.register(InventoryCountAsof)
admin.site.register(MaterialRequisition)
admin.site.register(SupplierRawMaterials)
