from django.contrib import admin
from .models import Post,Tag
# Register your models here.
#from django_markdown.admin import MarkdownModelAdmin

#class EntryAdmin(MarkdownModelAdmin):
    #list_display = ("title" , "created")
    #prepopulated_fields = {"slug" : ("title", )}

admin.site.register(Post)
admin.site.register(Tag)