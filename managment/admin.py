from django.contrib import admin
from django_singleton_admin.admin import DjangoSingletonModelAdmin

from .models import Case, CoreSettings, Dates, Document, Sponsors


class CaseAdmin(admin.ModelAdmin):
    list_display = (
        "case_name",
        "caseholder",
        "tasks",
    )
    list_filter = [
        "caseholder",
    ]


class DatesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date",
    )
    list_filter = [
        "date",
    ]


admin.site.register(CoreSettings, DjangoSingletonModelAdmin)
admin.site.register(Document)
admin.site.register(Sponsors)
admin.site.register(Dates, DatesAdmin)
admin.site.register(Case, CaseAdmin)
