from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#
#     # fieldsets = (
#     #     *UserAdmin.fieldsets,
#     #     (
#     #         'User role',
#     #         {
#     #             'fields': (
#     #                 'is_student',
#     #                 'is_teacher',
#     #                 'is_staff',
#     #
#     #             )
#     #         }
#     #     )
#     # )


admin.site.register(CustomUser,)
