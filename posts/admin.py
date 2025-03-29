from django.contrib import admin
from .models import Posts
# Register your models here.




class PostAdmin(admin.ModelAdmin):
    list_display=["id","post_title","post_content"]



admin.site.register(Posts, PostAdmin)  #we ca