#!/usr/bin/python3
import threading
from capstoneg08_client.Client import Client


class UserCommandHandler(threading.Thread):
    def __init__(self, myClient):
        threading.Thread.__init__(self)
        
        self.myClient = myClient
        self.myCommand = ''
    
    def handleUserCommand(self, myCommand):
        self.myCommand = myCommand
        
    def run(self):
        if self.myCommand == 'Hello World':
            self.myClient.sendMessageToServer('c'.encode())
        return
            