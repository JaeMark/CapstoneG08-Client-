#!/usr/bin/python3

from capstoneg08_client.Client import Client
from capstoneg08_usercommandhandler.UserCommandHandler import UserCommandHandler

def main():
    myClient = Client(8080, 'localhost')
    myClient.connectToServer
    isConnected = myClient.isConnected
    if isConnected:
        print("Client is running")
    if not isConnected:
        print("Client is not running")
    #print(myClient.isConnected)
    #myUserCommandHandler = UserCommandHandler(myClient)
    #txt = input("Enter command: ")
    #print("Nice to meet you! Your command was: " + txt)
    #if(myClient.isConnected == True):
    
    
main()