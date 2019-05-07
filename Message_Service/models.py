# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone


# Create your models here.


class FlightPlan(models.Model):
    # 航班计划
    Xml = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'FlightFPL'
        verbose_name = '航班计划表'
        verbose_name_plural = verbose_name


class PreliminaryFlightPlan(models.Model):
    # 初始飞行计划
    Xml = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'PreliminaryFPL'
        verbose_name = '初始飞行计划表'
        verbose_name_plural = verbose_name


class FiledFlightPlan(models.Model):
    # 拍发飞行计划
    Xml = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'FiledFPL'
        verbose_name = '拍发飞行计划表'
        verbose_name_plural = verbose_name


class ModifiedFlightPlan(models.Model):
    # 修改飞行计划
    Xml = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ModifiedFPL'
        verbose_name = '修改飞行计划表'
        verbose_name_plural = verbose_name
