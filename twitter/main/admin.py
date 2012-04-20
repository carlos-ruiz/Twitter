from django.contrib import admin
from main.models import User, Tweet


class UserAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('status', 'user',)

admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
