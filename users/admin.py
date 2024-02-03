from django.contrib import admin
from users.models import User
from basket.admin import BasketAdminInline
# Register your models here.



@admin.register(User)
class Admin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
