# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from users.models import User


# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User

    # Qué columnas ves en la tabla del admin
    list_display = ("email", "name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    # Cómo se ordena el listado
    ordering = ("email",)

    # Campos al buscar
    search_fields = ("email", "name")

    # Campos que se editan al abrir un usuario
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    # Campos cuando creas un usuario desde el admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "is_staff", "is_active"),
        }),
    )
