# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FlightPlan

import xml_analysis
from analysis_message import AnalysisMessage, ErrorMessage

# Create your views here.


class FlightPlanViews(APIView):
    # 航班计划接收
    def post(self, request, *args, **kwargs):
        data = request.body
        # print 'data', repr(data)
        et = request.data     # <lxml.etree._ElementTree object at 0x00000000058E4C88>  就是使用了parse得到的一个对象
        check = xml_analysis.basci_xml_check(et)
        if check:
            FlightPlan.objects.create(Xml=data)
            root = AnalysisMessage().analysis(request)
            return Response(root)
        else:
            error = ErrorMessage().error()
            return Response(error)


class PreliminaryFlightPlanViews(APIView):
    # 初始飞行计划接收
    pass


class FiledFlightPlanViews(APIView):
    # 拍发飞行计划接收
    pass


class ModifiedFlightPlanViews(APIView):
    # 修改飞行计划接收
    pass






