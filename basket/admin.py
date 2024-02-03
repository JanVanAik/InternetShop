from django.contrib import admin
from basket.models import Basket

# Register your models here.
admin.site.register(Basket)


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = readonly_fields = ('Product', 'quantity', 'created_timestamp')
    extra = 1