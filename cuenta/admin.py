from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# Unregister the default UserAdmin
admin.site.unregister(User)


# Define the function within admin.py

def get_id_usuario(obj):
    return f"{obj.id}".strip()
get_id_usuario.short_description = 'ID Usuario' # Sets the column header

def get_full_name(obj):
    return f"{obj.last_name}, {obj.first_name}".strip()
get_full_name.short_description = 'Nombre' # Sets the column header
get_full_name.admin_order_field = 'last_name' # Allows sorting by last name

def get_nombre_usuario(obj):
    return f"{obj.username}".strip()
get_nombre_usuario.short_description = 'Nombre Usuario' # Sets the column header


# Create a custom ModelAdmin class for the User
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Specify the columns you want to display in the list view
    list_display = (
         get_id_usuario,
         get_full_name, # Use the function reference here
        get_nombre_usuario,
        'is_active',
        #'email', # <-- Comment this out or remove it to hide the column
         )