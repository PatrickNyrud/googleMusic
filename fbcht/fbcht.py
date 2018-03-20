# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fbchat import Client
from fbchat.models import *
import time


def login():
    client = Client('xxx', 'xxx')
    get_msg(client)
    client.logout()

def get_msg(login_id):
    client = login_id

    messages = client.fetchThreadMessages(thread_id = "18", limit = 100)
    messages.reverse()
    for m in messages:
        print m.attachments

def spam_change(login_id):
    i = 2
    client = login_id
    user = client.searchForUsers('Håkon sd')
    while i < 15:
        client.changeNickname('Sugd ' + str(i) + ' kuker :)', user[0].uid, thread_id ="5862", thread_type = ThreadType.GROUP)
        i += 1
        time.sleep(1)

def spam_idiot():
    user = client.searchForUsers('Håkon sd')

    i = 0

    while 1:
        client.send(Message(text=':)'), thread_id=user[0].uid, thread_type=ThreadType.USER)
        print "Sendt " + str(i) + " smile fjes til ",
        print user[0].name.encode(encoding = "UTF-8")
        i += 1
        time.sleep(1)

login()
