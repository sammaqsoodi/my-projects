from django.contrib import admin
from .models import Profile

def make_published(modeladmin, request, queryset):

    result = queryset.update(status = 'published')

    if result == 1:
        message_bit = '1 post was'
    else:
        message_bit = "{} posts were".format(result)

    modeladmin.message_user(request, "{} successfully marked as published".format(message_bit))



def make_draft(modeladmin, request, queryset):

    result = queryset.update(status = 'draft')
    
    if result == 1:
        message_bit = '1 post was'
    else:
        message_bit = "{} posts were".format(result)

    modeladmin.message_user(request, "{} successfully marked as draft".format(message_bit))



make_published.short_description = 'منتشر کردن پست های انتتخاب شده'
make_draft.short_description = 'آماده انتشار کردن پست های لتخاب شده'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','curentCity')
    search_fields = ('user','curentCity')
    actions = [make_published, make_draft,]
