from django.contrib import admin
from userauths.models import User,Profile


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email',)
    search_fields=('username','email')
    list_filter=('username',)

class ProfileAdmin(admin.ModelAdmin):
    list_display=('full_name','gender')
    search_fields=('full_name','country')


admin.site.register(User,UserAdmin)
admin.site.register(Profile,ProfileAdmin)
