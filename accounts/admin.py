from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.


# class UserTypeInline(admin.StackedInline):
#     model = user_type
#     can_delete = False

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            # 'Franchise',
            # 'student',
            'user_type',
            'groups',
            # 'is_admin',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'is_staff',   'is_superuser','user_type',)
            }
        ),
    )

    list_display = ('username', 'name','is_superuser', 'user_type', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'user_type', 'is_active')
    search_fields = ('username',)
#     ordering = ('username',)
#     # inlines = (UserTypeInline, )
#     filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
