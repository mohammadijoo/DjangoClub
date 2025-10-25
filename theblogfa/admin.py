from django.contrib import admin
from .models import Postfa, Categoryfa
#, Profile, CustomComment
#Comment
from django_comments_xtd.admin import XtdCommentsAdmin
from django.utils.translation import gettext_lazy as _


admin.site.register(Postfa)
admin.site.register(Categoryfa)
# admin.site.register(Profile)
# admin.site.register(Comment)




# class CustomCommentAdmin(XtdCommentsAdmin):
#     list_display = ('title', 'cid', 'page', 'name', 'content_type',
#                     'object_pk', 'submit_date', 'followup', 'is_public',
#                     'is_removed')
#     list_display_links = ('cid', 'title')
#     fieldsets = (
#         (None,          {'fields': ('content_type', 'page', 'object_pk', 'site')}),
#         (_('Content'),  {'fields': ('title', 'user', 'user_name', 'user_email',
#                                   'user_url', 'comment', 'followup')}),
#         (_('Metadata'), {'fields': ('submit_date', 'ip_address',
#                                     'is_public', 'is_removed')}),
#     )

# admin.site.register(CustomComment, CustomCommentAdmin)