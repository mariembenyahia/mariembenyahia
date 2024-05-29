from django.contrib import admin
from .models import Operateur, User, Firewall, FirewallPolicy, SDWAN, SDWANRules


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email' , 'password')
admin.site.register(User, UserAdmin)

class OperateurAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' , 'numtel','password')

admin.site.register(Operateur, OperateurAdmin)

class FirewallAdmin(admin.ModelAdmin):
    list_display = ('ip', 'name' , 'description')
admin.site.register(Firewall, FirewallAdmin)

class FirewallPolicyAdmin(admin.ModelAdmin):
    list_display = ('name', 'source' , 'destination' , 'fortinet')
admin.site.register(FirewallPolicy, FirewallPolicyAdmin)

class SDWANAdmin(admin.ModelAdmin):
    list_display = ('sdwanzone', 'sdwanmembers' , 'gateway' , 'download', 'upload')
admin.site.register(SDWAN, SDWANAdmin)

class SDWANRulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'source' , 'destination' , 'members', 'fortigate')
admin.site.register(SDWANRules, SDWANRulesAdmin)


