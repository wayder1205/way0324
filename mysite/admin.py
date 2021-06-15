from django.contrib import admin
from mysite.models import Post, Country, City, TeamSite, StuSite

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','body')

admin.site.register(Post, PostAdmin)
admin.site.register(Country)

class CityAdmin(admin.ModelAdmin):
    list_display=('name','population','country')

admin.site.register(City, CityAdmin)
admin.site.register(TeamSite)
admin.site.register(StuSite)