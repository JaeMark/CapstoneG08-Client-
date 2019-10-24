#!/usr/bin/python3
#from capstoneg08_client.Client import Client

class ServerMessageHandler():
    def __init__(self, myClient):
        self.myClient = myClient
    
    def handleServerMessage(self, msg):
        serverMessage = ""
        serverMessage = msg.decode()
        print(serverMessage);
        return
    