from django.contrib import admin

from .models import Directions, Participants, Teams


class DirectionsAdmin(admin.ModelAdmin):
    list_display = ("direction",)
    list_filter = ["direction"]


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "patronymic",
        "email",
        "phone",
        "team",
    )
    list_filter = ["team"]


class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        "team_name",
        "organization",
        "direction",
    )
    list_filter = [
        "organization",
        "direction",
    ]


admin.site.register(Directions, DirectionsAdmin)
admin.site.register(Participants, ParticipantsAdmin)
admin.site.register(Teams, TeamsAdmin)
