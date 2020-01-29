from django.contrib import admin
from .models import TaxMob, NumMob


@admin.register(TaxMob)
class TaxMobAdmin(admin.ModelAdmin):
    list_display = ('name', 'opname',)
    list_filter = ('opname',)


@admin.register(NumMob)
class NumMobAdmin(admin.ModelAdmin):
    list_display = ('phone', 'get_op', 'TaxMob')
    list_filter = ('TaxMob__opname', 'TaxMob')

    def get_op(self, obj,):
        return obj.TaxMob.get_opname_display()
    get_op.short_description = 'мобільний оператор'
    get_op.admin_order_field = 'TaxMob__name'


