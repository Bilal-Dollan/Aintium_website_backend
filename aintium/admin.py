from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from aintium.models import User, AiModel, Request, Bookmark, Tag, Rate


class UserAdministrator(UserAdmin):
    list_display = (
        'email', 'username', 'phone', 'company', 'current_role', 'birth_date', 'date_joined',
        'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser',
        )
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdministrator)
admin.site.register(AiModel)
admin.site.register(Request)
admin.site.register(Bookmark)
admin.site.register(Tag)
admin.site.register(Rate)


