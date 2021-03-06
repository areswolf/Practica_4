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
from users.api import UserSignUpAPI, UserDetailAPI, BlogListAPI, BlogListSearchAPI
from users.views import BlogList, UserBlogList, UserBlogListFiltered, DevLog

urlpatterns = [
    #web
    url(r'^blogs/$', BlogList.as_view(), name='blog_list'),
    url(r'^blogs/(?P<username>\w+)$', UserBlogList.as_view(), name='user_blog_list'),
    url(r'^blogs/(?P<username>\w+)/categoria/(?P<cathegory>\w+)/$', UserBlogListFiltered.as_view(), name='user_post_detail_filtered'),
    #API
    url(r'^api/1.0/users/$', UserSignUpAPI.as_view(), name='user_sign_up_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),
    url(r'^api/1.0/blogs/$', BlogListAPI.as_view(), name='user_bloglist_api'),
    url(r'^api/1.0/blogs/(?P<username>\w+)/$', BlogListSearchAPI.as_view(), name='user_bloglistsearch_api'),
    #devlog
    url(r'^devlog/$', DevLog.as_view(), name='devlog'),





]
