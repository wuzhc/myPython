from django.conf.urls import patterns,include,url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"), #http://127.0.0.1:8000/post/1/
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
]

# urlpatterns = patterns('',
#     url(r'^$', views.post_list, name="post_list"),
#     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# )