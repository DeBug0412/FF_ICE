# -*- coding: utf-8 -*-

from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^FPL/$', views.FlightPlanViews.as_view(), name='FPL'),  # 航班计划接收
    url(r'^Preliminary_FPL/$', views.PreliminaryFlightPlanViews.as_view(), name='Preliminary_FPL'),  # 初始飞行计划接收
    url(r'^Filed_FPL/$', views.FiledFlightPlanViews.as_view(), name='Filed_FPL'),  # 拍发飞行计划接收
    url(r'^Modified_FPL/$', views.ModifiedFlightPlanViews.as_view(), name='Modified_FPL'),  # 修改飞行计划接收
]