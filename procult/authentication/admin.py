from django.contrib import admin
from .models import User, Ente
from .forms import EnteForm


class UserAdmin(admin.ModelAdmin):
    pass


class EnteAdmin(admin.ModelAdmin):
    form = EnteForm
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Ente, EnteAdmin)
