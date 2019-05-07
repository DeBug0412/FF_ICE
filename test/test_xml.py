#  coding: utf-8

from lxml import etree

tree = etree.parse("xml/text_xml")
# print tree
root = tree.getroot()
# print root

ns = {
    "fb": "http://www.fixm.aero/base/4.1",
    "xlink": "http://www.w3.org/1999/xlink",
    "fx": "http://www.fixm.aero/flight/4.1",
    "mesg": "http://www.fixm.aero/messaging/4.1",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}

# msgoriginator = root.find("mesg:messageOriginator", ns)
# if msgoriginator is not None:
#     for contact in msgoriginator.findall("fb:contact", ns):
#         onlinecontact = contact.find("fb:onlineContact", ns)
#         originator = onlinecontact.get('linkage')
#         print originator
#
# msgrecipient = root.find("mesg:recipient", ns)
# if msgrecipient is not None:
#     for contact in msgrecipient.findall("fb:contact", ns):
#         onlinecontact = contact.find("fb:onlineContact", ns)
#         recipient = onlinecontact.get("linkage")
#         print recipient
#
# flight = root.find('mesg:flight', ns)
# if flight is not None:
#     gufi = flight.find('fx:gufi', ns)
#     msggufi = gufi.get('codeSpace')
#     print msggufi
#
# flightplannegotiationstatus = root.find("mesg:flightPlanNegotiationStatus", ns)
# if flightplannegotiationstatus is not None:
#     filingstatus = flightplannegotiationstatus.find("mesg:filingStatus", ns)
#     status = filingstatus.get("status")
#     print status


ns_full = {
    'fb': '{http://www.fixm.aero/base/4.1}',
    'fx': '{http://www.fixm.aero/flight/4.1}',
    'mesg': '{http://www.fixm.aero/messaging/4.1}',
    'xlink': '{http://www.w3.org/1999/xlink}',
}
#
msgOriginator = root.find("mesg:messageOriginator", ns)  # 发送者
if msgOriginator is not None:
    # print msgOriginator
    for contact in msgOriginator.findall("fb:contact", ns):
        # print contact
        onlineContact = contact.find("fb:onlineContact", ns)
        # print onlineContact.get('linkage')
#
recipient = root.find("mesg:recipient", ns)  # 接收者
if recipient is not None:
    # print recipient
    for contact in recipient.findall("fb:contact", ns):
        # print contact
        onlineContact = contact.find("fb:onlineContact", ns)
        # print onlineContact.get("linkage")
        rec = onlineContact.get('linkage')

flight = root.find('mesg:flight', ns)
if flight is not None:
    gufi = flight.find('fx:gufi', ns)
    msggufi = gufi.get('codeSpace')
    uuid = gufi.text
    print msggufi


 #  add messageOriginator
contact = etree.Element(ns_full["fb"] + "contact")  # 拼接发送者
onlineContact = etree.Element(ns_full["fb"] + "onlineContact")
msg = etree.Element(ns_full["mesg"] + "messageOriginator")
onlineContact.set("linkage", "FPLmanagementCenter")
contact.append(onlineContact)
msg.append(contact)
_originator = root.insert(0, msg)
print _originator

contact = etree.Element(ns_full["fb"] + "contact")  # 拼接接收者
onlineContact = etree.Element(ns_full["fb"] + "onlineContact")
msg = etree.Element(ns_full["mesg"] + "recipient")
onlineContact.set("linkage", "hangsi")
contact.append(onlineContact)
msg.append(contact)
_recipient = root.insert(1, msg)
print _recipient

gufi = etree.Element(ns_full['mesg'] + "uniqueMessageIdentifier")
gufi.set("codeSpace", "zzzz")
gufi.set("statusReason", "ok")

_gufi = root.insert(-1, gufi)
print _gufi


import uuid
print str(uuid.uuid4())





