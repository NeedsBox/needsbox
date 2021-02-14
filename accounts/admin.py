from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_admin')
    readonly_fields = ('date_joined', 'last_login')

    fields = (
        'username',
        'password',
        'name',
        'email',
        'profile_image',
        'biography',
        'website',
        'contact',
        'account_type',
        'is_active',
        'is_staff',
        'date_joined',
        'last_login',
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'name',
                'email',
                'password1',
                'password2',
                'account_type',
                'is_staff',
                'is_active')}
         ),
    )


admin.site.register(Account, AccountAdmin)
