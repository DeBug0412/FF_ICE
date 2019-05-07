# coding: utf-8
import codecs
import lxml
from django.utils import six
from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError
from rest_framework.settings import api_settings


from django.conf import settings


class XmlParser(BaseParser):
    media_type = 'application/xml'

    def parse(self, stream, media_type=None, parser_context=None):

        try:
            return lxml.etree.parse(stream)
        except Exception as exc:
            raise ParseError('lxml parse error - %s' % six.text_type(exc))










