from django.contrib import admin
from .models import User, Ente


class UserAdmin(admin.ModelAdmin):
    pass


class EnteAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Ente, EnteAdmin)
