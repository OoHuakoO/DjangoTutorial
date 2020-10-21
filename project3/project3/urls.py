"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views
urlpatterns = [

    path('about/',views.about),
    path('detail/',views.detail),
    path('order/',views.order),
    path('variable/',views.variable),
    path('tag/if/', views.tag_if),
    path('tag/for/', views.tag_for),
    path('tag/other/', views.tag_other),
    path('', views.index, name='index'),
    path('tag/auto-escape/', views.tag_auto_escape),
    path('filter/str-list-num/', views.filter_str_list_num),
    path('filter/num/', views.filter_num),
    path('filter/string/', views.filter_string),
    path('filter/list',views.filter_list),
    path('filter/special-chars/', views.filter_special_chars),
    path('filter/url/', views.filter_url),
    path('filter/datetime/', views.filter_datetime),
    path('filter/custom/', views.filter_custom)
]
