
from django.conf.urls import include, url
from django.contrib import admin

from app01 import views

urlpatterns = [

    url(r"^index$",views.index),
    url(r'^set_session$', views.set_session),           # 保存session数据
    url(r'^get_session$', views.get_session),
    url(r'^hget_cart$',views.hget_cart)
]
