from lxml import etree

# as the web process start from the base dir
xmlschema_f = open("xml_core/messaging/Messaging.xsd", "rb")
xmlschema_doc = etree.parse(xmlschema_f)
xmlschema = etree.XMLSchema(xmlschema_doc)


def basci_xml_check(xml):


    # try:
    #     doc = etree.fromstring(xml)
    # except (etree.ParseError, ValueError) as exc:
    #     return False, str(exc)
    if xmlschema.validate(xml):
        return True, None
    else:
        # log = xmlschema.error_log
        # error = log.last_error
        return False,  # error
