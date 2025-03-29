from django.contrib import admin
from .models import Posts
# Register your models here.




@admin.register(Posts)   #if used this dont use code at line 14
class PostAdmin(admin.ModelAdmin):
    list_display=["id","post_title","post_content"]



admin.site.register(Posts, PostAdmin)  #we can use code at line 7 except this line