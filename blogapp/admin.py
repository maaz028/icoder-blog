from django.contrib import admin

from blogapp.models import post, comment,comment_reply



from django.db import models
# Register your models here.


admin.site.site_header='ICoder Admin Section'
admin.site.site_title='Admin Panel'
admin.site.index_title='Administration'

admin.site.register((comment, comment_reply))
admin.site.register(post)
