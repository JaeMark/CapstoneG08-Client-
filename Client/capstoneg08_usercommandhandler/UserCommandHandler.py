#!/usr/bin/python3
from capstoneg08_client.Client import Client

class UserCommandHandler():
    def __init__(self, myClient):
        self.myClient = myClient;
    
    def handleUserCommand(self, myCommand):
        self.myCommand = myCommand
        myCommandThread = UserCommandHandler(self.myClient)
        myCommandThread.start()
        
    def run(self):
        if self.myCommand == 'Hello World':
            self.myClient.sendMessageToServer('h')
        return
            