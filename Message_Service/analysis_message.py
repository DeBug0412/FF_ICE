# coding: utf-8
from lxml import etree
import uuid

import xml_analysis

ns = {
    "fb": "http://www.fixm.aero/base/4.1",
    "xlink": "http://www.w3.org/1999/xlink",
    "fx": "http://www.fixm.aero/flight/4.1",
    "mesg": "http://www.fixm.aero/messaging/4.1",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}

ns_full = {
    'fb': '{http://www.fixm.aero/base/4.1}',
    'fx': '{http://www.fixm.aero/flight/4.1}',
    'mesg': '{http://www.fixm.aero/messaging/4.1}',
    'xlink': '{http://www.w3.org/1999/xlink}',
}


class AnalysisMessage(object):

    def analysis(self, request, *args, **kwargs):

        originator = None
        recipient = None
        msggufi = None
        status = None

        tree = request.data
        root = tree.getroot()
        msgoriginator = root.find("mesg:messageOriginator", ns)  # 解析发送者
        if msgoriginator is not None:
            for orcontact in msgoriginator.findall("fb:contact", ns):
                oronlinecontact = orcontact.find("fb:onlineContact", ns)
                originator = oronlinecontact.get('linkage')
                _originator = oronlinecontact.set('linkage', "FPLmanagementCenter")  # 拼接发送者

        msgrecipient = root.find("mesg:recipient", ns)   # 解析接收者
        if msgrecipient is not None:
            for recontact in msgrecipient.findall("fb:contact", ns):
                reonlinecontact = recontact.find("fb:onlineContact", ns)
                recipient = reonlinecontact.get("linkage")


        flight = root.find('mesg:flight', ns)  # 解析gufi
        if flight is not None:
            gufi = flight.find('fx:gufi', ns)
            msggufi = gufi.get('codeSpace')

        flightplannegotiationstatus = root.find("mesg:flightPlanNegotiationStatus", ns)  # 解析状态码
        if flightplannegotiationstatus is not None:
            filingstatus = flightplannegotiationstatus.find("mesg:filingStatus", ns)
            status = filingstatus.get("status")


        #  joint

        root = etree.Element(ns_full["mesg"] + "Message")

        contact = etree.Element(ns_full["fb"] + "contact")  # 拼接委托者
        onlineContact = etree.Element(ns_full["fb"] + "onlineContact")
        deliveryResponsibility = etree.Element(ns_full["mesg"] + "deliveryResponsibility")
        onlineContact.set("linkage", "FPLmanagementCenter")
        contact.append(onlineContact)
        deliveryResponsibility.append(contact)
        root.insert(0,deliveryResponsibility)

        contact = etree.Element(ns_full["fb"] + "contact")  # 拼接发送者
        onlineContact = etree.Element(ns_full["fb"] + "onlineContact")
        msg = etree.Element(ns_full["mesg"] + "messageOriginator")
        onlineContact.set("linkage", "FPLmanagementCenter")
        contact.append(onlineContact)
        msg.append(contact)
        root.insert(1, msg)

        contact = etree.Element(ns_full["fb"] + "contact")  # 拼接接收者
        onlineContact = etree.Element(ns_full["fb"] + "onlineContact")
        msg = etree.Element(ns_full["mesg"] + recipient)
        onlineContact.set("linkage", originator)
        contact.append(onlineContact)
        msg.append(contact)
        root.insert(2, msg)

        uniqueMessageIdentifier = etree.Element(ns_full['mesg'] + "uniqueMessageIdentifier")  # uuid
        uniqueMessageIdentifier.set("codeSpace", msggufi)
        _uuid = str(uuid.uuid4())
        uniqueMessageIdentifier.text = _uuid
        root.insert(3, uniqueMessageIdentifier)

        submissionStatus = etree.Element(ns_full["mesg"] + "submissionStatus")
        submissionStatus.set("status", "ACK")
        submissionStatus.set("statusReason", "")
        root.insert(4, submissionStatus)
        print etree.tostring(root)
        return etree.tostring(root)


class ErrorMessage(object):
    """
    当校验不通过时 使用自行构造的xml错误报文
    """
    def error(self):
        root = etree.Element(ns_full['mesg'] + "Message")  # 构造Element

        contact = etree.Element(ns_full["fb"] + "contact")  # 构造发起者
        onlineContact = etree.Element(ns_full["fb"] + "onlineContact")
        msg = etree.Element(ns_full["mesg"] + "messageOriginator")
        onlineContact.set("linkage", "FPLmanagementCenter")
        contact.append(onlineContact)
        msg.append(contact)
        root.insert(0, msg)

        uniqueMessageIdentifier = etree.Element(ns_full['mesg'] + "uniqueMessageIdentifier")  # uuid
        uniqueMessageIdentifier.set("codeSpace", "urn:uuid")
        _uuid = str(uuid.uuid4())
        uniqueMessageIdentifier.text = _uuid
        root.insert(1, uniqueMessageIdentifier)

        submissionStatus = etree.Element(ns_full["mesg"] + "submissionStatus")  # 构造错误信息
        submissionStatus.set("status", "Reject")
        submissionStatus.set("statusReason", "XML报文格式校验未通过")
        root.insert(2, submissionStatus)

        return etree.tostring(root)




