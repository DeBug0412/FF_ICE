# coding: utf-8

import redis


class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host="localhost")
        # 频道名称
        self.chan_sub = "Msg_Service"

    def public(self, msg):
        """
        在指定频道上发布消息
        :param msg:
        :return:
        """
        # publish(): 在指定频道上发布消息，返回订阅者的数量
        self.__conn.publish(self.chan_sub, msg)
        return True

    def subscribe(self):
        # 返回发布订阅对象，通过这个对象你能1,订阅频道 2,监听频道中的消息
        pub = self.__conn.pubsub()
        # 订阅某个频道，与publish()中指定的频道一样。消息会发布到这个频道中
        pub.subscribe(self.chan_sub)
        return pub