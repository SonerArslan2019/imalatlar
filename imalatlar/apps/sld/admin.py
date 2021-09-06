from django.contrib import admin

from .models import SLD

admin.site.register(SLD)


class SLDAdmin(admin.ModelAdmin):
    search_fields = ("company_name", "crm", "door_type")
    list_display = (
        'drawing', 'delivery_date', 'created_time'
    )


admin.site.site_header = "ARSLAN YAPI (Imalat) YONETIM PANELI"
