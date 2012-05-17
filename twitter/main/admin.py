from django.contrib import admin
from main.models import UserProfile, Tweet


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'birthday',)
	search_fields = ('user',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('owner', 'status',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tweet, TweetAdmin)
