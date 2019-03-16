from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import MyUser, MyUserProfile, AccountsToken
from accounts.forms import UserChangeForm, UserCreationForm




class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'prenom', 'is_active',)
    list_filter  = ('is_active',)
    readonly_fields = ('password',)
    search_fields = ['nom', 'prenom', 'email']

class MyUserProfileAdmin(admin.ModelAdmin):
    actions      = ('activer_compte', 'desactiver_compte',)
    list_display = ('myuser_id', 'telephone',)
    search_fields = ['myuser_id__nom', 'myuser_id__prenom', 'myuser_id__email']

    def activer_compte(self, request, queryset):
        queryset.update(actif=True)

    def desactiver_compte(self, request, queryset):
        queryset.update(actif=False)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyUserProfile, MyUserProfileAdmin)
admin.site.register(AccountsToken)
admin.site.unregister(Group)
