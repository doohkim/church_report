from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'recent_attend_date', 'last_login_at', 'is_superuser', 'is_active')
    list_display_links = ('id', 'email')
    exclude = ('password',)

    def created(self, obj):
        return obj.created.strftime("%Y-%m-%d")

    def recent_attend_date(self, obj):
        if not obj.recent_attend_date:
            return ''
        return obj.recent_attend_date.strftime("%Y-%m-%d")

    def last_login_at(self, obj):
        if not obj.last_login:
            return ''
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    created.admin_order_field = '-created'  # 가장 최근에 가입한 사람부터 리스팅
    created.short_description = '가입일'
    recent_attend_date.admin_order_field = "-recent_attend_date"
    recent_attend_date.short_description = '최근 출석일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_description = '최근로그인'
