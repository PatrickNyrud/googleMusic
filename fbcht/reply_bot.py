# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fbchat import Client
from fbchat.models import *


class replayBot(Client):
    def onMessage(self, author_id, message, thread_id, **kwargs):
        print "Fikk en medling: " + str(message)
        user = client.searchForUsers('Håkon asd')

        if author_id == user[0].uid:
            print "Sente en mld"
            self.send(Message(text = ":)"), thread_id = thread_id, thread_type = ThreadType.USER)

client = replayBot("xxxx", "xxxx")
client.listen()

