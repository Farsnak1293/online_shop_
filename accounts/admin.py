from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm,CustomUserCreationForm
from .forms import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username',)
