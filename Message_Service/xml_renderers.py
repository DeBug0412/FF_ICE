# coding: utf8

from rest_framework.renderers import BaseRenderer


class XmlRenderers(BaseRenderer):

    media_type = 'application/xml'
    format = 'xml'
    charset = None

    def render(self, data, media_type=None, renderer_context=None):
        print data
        return data
