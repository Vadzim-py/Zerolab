from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    search_fields = ('username',)
    list_per_page = 5
    list_max_show_all = 200
    actions = []





