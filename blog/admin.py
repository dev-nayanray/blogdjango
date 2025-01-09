from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category')
    search_fields = ('title', 'content', 'category')
    list_filter = ('category',)
    date_hierarchy = 'created_at'

# admin.py
from django.contrib import admin
from .models import ContactInfo

admin.site.register(ContactInfo)

# blog/admin.py

from django.contrib import admin
from .models import TeamMember

# Register the TeamMember model to the admin interface
admin.site.register(TeamMember)
