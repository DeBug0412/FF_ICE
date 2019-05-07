# coding: utf-8


from rest_framework import serializers
from .models import FiledFlightPlan, FlightPlan, PreliminaryFlightPlan, ModifiedFlightPlan


class FlightPlanSerializer(serializers.ModelSerializer):  # 航班计划

    class Meta:
        model = FlightPlan
        fields = '__all__'


class PreliminaryFlightPlanSerializer(serializers.ModelSerializer):  # 初始飞行计划

    class Meta:
        model = PreliminaryFlightPlan
        fields = '__all__'


class FiledFlightPlanSerializer(serializers.ModelSerializer):  # 拍发飞行计划

    class Meta:
        model = FiledFlightPlan
        fields = '__all__'


class ModifiedFlightPlanSerializer(serializers.ModelSerializer):  # 修改飞行计划

    class Meta:
        model = ModifiedFlightPlan
        fields = '__all__'
