# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fbchat import Client
from fbchat.models import *

def login():
    client = Client("nyrud96@gmail.com", "Totlikep67i8")

    print client.uid

    logout(client)


def logout(usr_id):
    client = usr_id
    client.logout()

login()
