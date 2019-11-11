"""User admin classes."""
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User

# Models
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username'
        'user__first_name',
        'user__last_name',
        'phone_number')

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modify'
        )

    fieldsets =(
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography',)
            ),
        }),
        ('Metadata', {
            'fields':(
                ('created', 'modify'),
            ),
        })
        )

    readonly_fields = ('created', 'modify')




class ProfileInline(admin.StackedInline):
    """Profile inline admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to  base user admin."""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
