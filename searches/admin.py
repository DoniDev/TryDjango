from django.contrib import admin
from . models import SearchQuery

@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ['user', 'query','id']

