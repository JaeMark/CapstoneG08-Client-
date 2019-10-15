#!/usr/bin/python3
import threading
from capstoneg08_client.Client import Client
from capstoneg08_usercommandhandler.UserCommandHandler import UserCommandHandler

BUFF_SIZE = 1024

def main():
    myClient = Client(BUFF_SIZE, 'localhost', 8080)
    myClient.start()

    # connection test
    isConnected = myClient.isConnected
    if isConnected:
        print("Client is running")
    if not isConnected:
        print("Client is not running")

    myUserCommandHandler = UserCommandHandler(myClient)
    txt = input("Enter command: ")
    myUserCommandHandler.handleUserCommand(txt)
    myUserCommandHandler.start()
    
    
main()