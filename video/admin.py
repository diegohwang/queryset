from django.contrib import admin

# Register your models here.

from models import site, media

class MediaAdmin(admin.ModelAdmin):
    list_display=('title', 'url')
    
class SiteAdmin(admin.ModelAdmin):
    list_dislplay=('site_name')
    
admin.site.register(site,SiteAdmin)
admin.site.register(media,MediaAdmin)