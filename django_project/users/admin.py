from django.contrib import admin
from .models import Profile

"""class blogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_posted")
    search_fields = ("title", "author", "date_posted")
    readonly_fields = ("title", "author", "date_posted")
 """   
admin.site.register(Profile)
