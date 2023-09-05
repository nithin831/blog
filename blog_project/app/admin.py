from django.contrib import admin
from app.models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ["title","author","publish","created","update","body", "status", "slug"]
	list_filter =  ["author","status"]
	search_fields = ["title"]
	raw_id_fields = ["author"] #used in providing author as id (i.e, 1->nithin,.....)
	prepopulated_fields = {"slug":["title"]}
	ordering = ["status", "publish"]

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ["name", "email" , "comment", "post", "created","update","active"]
	list_filter =  ["post","active", "created"]
	search_fields = ["post","name"]

admin.site.register(Comment,CommentAdmin)



# user - nithin
# password - QWer123@#