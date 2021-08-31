
from django.contrib import admin
from django.urls import path, include
from .import views
from home import views as v

urlpatterns = [
    path('', views.index, name='index'),
    path('post_view/<int:id>', views.post_view, name='post_view'),
    path('search_data', views.search_data, name='search_data'),
    path('signup', v.handle_signup,name='signup'),
    path('comment/<int:postid>', views.post_comment,name='comment'),
    path('post_view/logout', v.handle_logout),
    path('reply/<int:postid>/<int:sno>', views.handle_reply, name='reply'),
    path('delete/<int:rid>/<int:pid>', views.delete_rply,name='delete'),
    path('delete_comment/<int:cid>/<int:pid>', views.delete_comment,name='delete_comment'),
    path('write_blog',views.create_blog,name='create_blog'),
    path('save_blog',views.save_blog,name='save_blog')
   
]
