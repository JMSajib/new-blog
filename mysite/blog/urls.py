from django.conf.urls import url
from django.urls import path
from blog.views import post_list, post_detail, PostListView, post_share

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('post/<int:post_id>/share/', post_share, name='post_share'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    
]