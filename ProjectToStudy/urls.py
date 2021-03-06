"""ProjectToStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ProjectToStudy.views import *
from bookdb.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^now/$',now),
    url(r'^now/plus/(\d{1,2})/$',after_now),
    url(r'^$',book_list),
    url(r'^search/$',searchAuthor),
    url(r'^searchResult/(?P<auid>\w+)/$',searchResult),
    url(r'^update_book/(\d+)/$',update_book),
    url(r'^update_author/(\d+)/$',update_author),
    url(r'^detail/(?P<isbn>\w+)/$',detail),
    url(r'^delete/(\d+)/$',delete),
    url(r'^add/$',add),
]
