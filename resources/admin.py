from django.contrib import admin

from .models import UserProfile, Resource, Comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Resource)
admin.site.register(Comment)