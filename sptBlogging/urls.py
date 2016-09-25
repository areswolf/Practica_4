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
from users.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView
from blog import urls as blogs_urls
from users import urls as users_urls

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    # Registration
    url(r'^', include('registration.backends.default.urls')),
    url(r'signup$', RegistrationView.as_view(form_class = ExRegistrationForm), name = 'registration_register'),

    # Blogs (posts)
    url(r'', include(blogs_urls)),

    # users (Blogs)
    url(r'', include(users_urls)),
]
