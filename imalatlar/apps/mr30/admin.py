from django.contrib import admin

from .models import MR30

admin.site.register(MR30)


class SLDAdmin(admin.ModelAdmin):
    search_fields = ("company_name", "crm", "door_type")
    list_display = (
        'drawing', 'delivery_date', 'created_time'
    )


admin.site.site_header = "ARSLAN YAPI (Imalat) YONETIM PANELI"

