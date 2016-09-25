"""sptBlogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url

from blog.api import PostListAPI, PostDetailAPI, PostListSearchAPI
from blog.views import Home, user_post_detail, homeFiltered, newPost

urlpatterns = [
    #Web
    url(r'^$', Home.as_view(), name='home'),
    url(r'^(?P<cathegory>\w+)$', homeFiltered.as_view(), name='home_filtered'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$', user_post_detail.as_view(), name='user_post_detail'),
    url(r'^newpost/$', newPost.as_view(), name='new_post'),
    #API
    url(r'^api/1.0/posts/$', PostListAPI.as_view(), name='blogs_postlist_api'),
    url(r'^api/1.0/posts/(?P<title_content>\w+)$', PostListSearchAPI.as_view(), name='blogs_postlistsearch_api'),
    url(r'^api/1.0/posts/(?P<pk>[0-9]+)$', PostDetailAPI.as_view(), name='blogs_postdetail_api'),
]