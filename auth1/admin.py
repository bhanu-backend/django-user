from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils.html import format_html
import pprint



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'decoded_data', 'expire_date']

    def decoded_data(self, obj):
        try:
            data = obj.get_decoded()
            return format_html("<pre>{}</pre>", pprint.pformat(data))
        except Exception as e:
            return f"Error decoding: {e}"

    decoded_data.short_description = 'Session Data'

# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display = ['session_key', 'session_data', 'expire_date']


# admin.site.register(Session)