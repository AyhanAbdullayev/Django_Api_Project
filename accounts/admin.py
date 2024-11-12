from django.contrib import admin
from accounts.models  import User,BlackListIpAdress





@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ["id","username","first_name","last_name","email","is_staff","is_active","date_joined","last_login"]


@admin.register(BlackListIpAdress)

class BlockListedApi(admin.ModelAdmin):
    list_display = ["id","ip_adress"]
    list_display_links = ["id"]


