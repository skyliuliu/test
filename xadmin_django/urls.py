"""xadmin_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from app.views import UserViews, RegViews, CacheView, index, GroupViews, MemberViews
admin.autodiscover()

router = DefaultRouter()
router.register(r'users', UserViews)
router.register(r'reg', RegViews, base_name='r')
router.register(r'group', GroupViews, base_name='group')
router.register(r'member', MemberViews, base_name='member')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^index/$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^cache/', CacheView.as_view()),
    url(r'^docs/', include_docs_urls(title='API Doc')),
]
