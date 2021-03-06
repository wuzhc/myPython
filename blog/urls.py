from django.conf.urls import patterns,include,url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"), #http://127.0.0.1:8000/post/1/
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/draft/$', views.post_draft_list, name="post_draft_list"),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^posts/search/$', views.full_search, name='full_search'),
]

# urlpatterns = patterns('',
#     url(r'^$', views.post_list, name="post_list"),
#     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# )