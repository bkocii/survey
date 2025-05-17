from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, UserProfile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'is_staff', 'is_superuser']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Roles', {'fields': ('is_panelist',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_panelist', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    filter_horizontal = ()

admin.site.register(UserProfile)

