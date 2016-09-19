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
from users.views import blog_list, user_blog_list, user_blog_list_filtered


urlpatterns = [
    url(r'^blogs/$', blog_list.as_view(), name='blog_list'),
    url(r'^blogs/(?P<username>\w+)$', user_blog_list.as_view(), name='user_blog_list'),
    url(r'^blogs/(?P<username>\w+)/categoria/(?P<cathegory>\w+)/$', user_blog_list_filtered.as_view(), name='user_post_detail_filtered'),

]
