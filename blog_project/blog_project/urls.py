"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.list_view , name = "home"),
    # path("", v.List_view.as_view()),
    re_path(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$", v.detail_view, name = "detail"),
    re_path(r"^(?P<id>\d+)/share/$", v.share_mail),
    re_path(r"^tag/(?P<tag_slug>[-\w]+)/$", v.list_view, name = "tags_nk"),

]
