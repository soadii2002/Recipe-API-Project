'''
    django admin customization for the core app.
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as trans
from core import models


class UserAdmin(BaseUserAdmin):
    ''' Define the admin pages for users.'''
    ordering = ['id']

    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email','password')}),
        (trans('Personal Info'), {'fields': ('name',)}),
        (
            trans('premissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (trans('important dates'), {'fields': ('last_login',)}
        )
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : (
                'email',
                'name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )
admin.site.register(models.User, UserAdmin)