from django.contrib import admin
from rest_framework2.authtoken.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)


admin.site.register(Token, TokenAdmin)
