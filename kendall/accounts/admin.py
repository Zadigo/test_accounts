from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import AccountsToken, MyUser, MyUserProfile


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'prenom', 'is_active',)
    list_filter  = ('is_active',)
    readonly_fields = ('password',)
    search_fields = ['nom', 'prenom', 'email']

class MyUserProfileAdmin(admin.ModelAdmin):
    actions      = ('activer_compte', 'desactiver_compte',)
    list_display = ('myuser', 'telephone',)
    search_fields = ['myuser__nom', 'myuser__prenom', 'myuser__email']

    def activer_compte(self, request, queryset):
        queryset.update(actif=True)

    def desactiver_compte(self, request, queryset):
        queryset.update(actif=False)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyUserProfile, MyUserProfileAdmin)
admin.site.register(AccountsToken)
admin.site.unregister(Group)
