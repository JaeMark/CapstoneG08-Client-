#!/usr/bin/python3

from capstoneg08_client.Client import Client
from capstoneg08_usercommandhandler.UserCommandHandler import UserCommandHandler

def main():
    myClient = Client(8080, 'localhost')
    myUserCommandHandler = UserCommandHandler(myClient)
    txt = input("Enter command: ")
    print("Nice to meet you! Your command was: " + txt)
    
main()