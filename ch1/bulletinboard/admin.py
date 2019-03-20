from django.contrib import admin
from .models import Bulletinboard, Comment
#패스워드 추가 바뀐부분
class BulletinboardAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer','password']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['writer', 'text']
    
admin.site.register(Bulletinboard, BulletinboardAdmin)
admin.site.register(Comment, CommentAdmin)
