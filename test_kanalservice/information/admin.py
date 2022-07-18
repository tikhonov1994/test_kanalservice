from django.contrib import admin

from information.models import ExchangeRate, Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    pass
