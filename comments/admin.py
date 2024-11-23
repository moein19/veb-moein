from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Comments
from bloggers.models  import Blogger


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blogger','post_title',
    'comment_date','post_id')
    list_display_links = ["blogger"]
    search_fields = ['blogger','comment_text']
    list_filter = ["blogger"]
    readonly_fields = ['blogger']
    list_per_page = 5


    def save_model(self, request, obj, form, change) -> None:
        obj.blogger = Blogger.objects.filter(user = request.user).first()
        return super().save_model(request, obj, form, change)


    def get_queryset(self, request):
        qs = super(CommentAdmin,self).get_queryset(request)

        if request.user.is_superuser:
            return qs
        
        return qs.filter(blogger__user = request.user)



    
   



admin.site.register(Comments,CommentAdmin)
