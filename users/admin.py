from typing import Any

from django.contrib import admin
from django.forms.models import ModelForm
from django.http import HttpRequest

from users.models import User
from users.forms import UserCreation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreation
    list_display = ('username', 'email', 'role', 'is_staff')
    list_display_links = ('username',)
    list_editable = ('email', 'role', 'is_staff')

    # When creating a new user in the admin
    def get_fieldsets(self, request: HttpRequest, obj: Any | None = None) -> list[tuple[str | None, dict[str, Any]]]:
        if not obj:
            return [
                (None, {
                    'classes': ('wide',),
                    'fields': ('email', 'username', 'role', 'password1', 'password2')
                }
                ),
            ]
        return super().get_fieldsets(request, obj)

    def get_form(self, request: HttpRequest, obj: Any | None = None,
                 change: bool = False, **kwargs: Any) -> type[ModelForm]:
        if not obj:
            kwargs['form'] = self.add_form
        return super().get_form(request, obj, change, **kwargs)
