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

from django.conf.urls import url, include
from django.contrib import admin
from blog.views import home, user_post_detail, newPost, homeFiltered
from users.views import blog_list, user_blog_list, user_blog_list_filtered
from users.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('registration.backends.default.urls')),
    url(r'signup$', RegistrationView.as_view(form_class = ExRegistrationForm), name = 'registration_register'),

    url(r'^$', home, name='home'),
    url(r'^(?P<cathegory>\w+)$', homeFiltered.as_view(), name='home_filtered'),

    url(r'^blogs/$', blog_list.as_view(), name='blog_list'),
    url(r'^blogs/(?P<username>\w+)$', user_blog_list.as_view(), name='user_blog_list'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$', user_post_detail.as_view(), name='user_post_detail'),

    url(r'^blogs/(?P<username>\w+)/categoria/(?P<cathegory>\w+)/$', user_blog_list_filtered.as_view(), name='user_post_detail_filtered'),

    url(r'^newpost/$', newPost.as_view(), name='new_post'),

]
